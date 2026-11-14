#!/bin/bash
set -euo pipefail

REGION="us-east-1"
APP_DIR="/opt/lab6-usuarios-aws"
REPOSITORY="https://github.com/Miguel-ACD/lab6-usuarios-aws.git"

dnf install -y docker git
systemctl enable --now docker

rm -rf "$APP_DIR"
git clone --depth 1 "$REPOSITORY" "$APP_DIR"
cd "$APP_DIR"

read_parameter() {
  aws ssm get-parameter \
    --region "$REGION" \
    --name "$1" \
    --with-decryption \
    --query 'Parameter.Value' \
    --output text
}

DB_ENDPOINT="$(read_parameter /lab6/db/endpoint)"
DB_PASSWORD="$(read_parameter /lab6/db/password)"
DJANGO_SECRET="$(read_parameter /lab6/django/secret)"
ADMIN_PASSWORD="$(read_parameter /lab6/admin/password)"

TOKEN="$(curl -sS -X PUT -H 'X-aws-ec2-metadata-token-ttl-seconds: 21600' http://169.254.169.254/latest/api/token)"
PUBLIC_IP="$(curl -sS -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4)"

cat > .env <<EOF
DJANGO_SECRET_KEY=$DJANGO_SECRET
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=$PUBLIC_IP,localhost,127.0.0.1
DJANGO_CSRF_TRUSTED_ORIGINS=http://$PUBLIC_IP:8000

POSTGRES_DB=lab6
POSTGRES_USER=lab6admin
POSTGRES_PASSWORD=$DB_PASSWORD
POSTGRES_HOST=$DB_ENDPOINT
POSTGRES_PORT=5432

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@lab6.local
DJANGO_SUPERUSER_PASSWORD=$ADMIN_PASSWORD

AWS_STORAGE_BUCKET_NAME=lab6-usuarios-304318513298-us-east-1
AWS_S3_REGION_NAME=$REGION
EOF

chmod 600 .env
docker build -t lab6-usuarios:latest .
docker rm -f lab6-usuarios 2>/dev/null || true
docker run -d \
  --name lab6-usuarios \
  --restart unless-stopped \
  --env-file .env \
  -p 8000:8000 \
  lab6-usuarios:latest

echo "Lab6 deployment completed at http://$PUBLIC_IP:8000" > /opt/lab6-ready
