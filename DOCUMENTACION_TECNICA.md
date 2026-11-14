# Documentación técnica del Laboratorio 6

## Datos académicos

- Estudiante: Miguel Angel Champi Hinojosa
- Código: 202110072
- Curso: Introducción a Cognitive Computing
- Docente: Farfán Madariaga, Jaime Moshe

## Repositorio de la actividad 1

Código, instrucciones y evidencias: https://github.com/Miguel-ACD/lab6-usuarios-aws

## Alcance implementado

La aplicación permite que un administrador autenticado cree, consulte, actualice y elimine usuarios. Cada usuario puede tener nombre, correo, teléfono, rol, estado y foto de perfil.

## Arquitectura

1. El navegador accede al panel Django publicado por el puerto 8000.
2. Django se ejecuta con Gunicorn dentro de un contenedor Docker en Amazon EC2.
3. Los usuarios y perfiles se guardan en Amazon RDS PostgreSQL.
4. Las fotos se almacenan como objetos privados en Amazon S3.
5. EC2 utiliza un rol IAM para acceder a S3 y Parameter Store sin claves permanentes.

## Recursos desplegados

| Servicio | Recurso | Configuración principal |
|---|---|---|
| EC2 | `lab6-usuarios-ec2` | `t3.micro`, Amazon Linux 2023, Docker |
| RDS | `lab6-postgres` | PostgreSQL, `db.t4g.micro`, 20 GB, no público |
| S3 | `lab6-usuarios-304318513298-us-east-1` | Acceso público bloqueado y cifrado AES-256 |
| IAM | `lab6-ec2-role` | Acceso limitado a S3, SSM y Parameter Store |
| Parameter Store | `/lab6/*` | Contraseñas y secreto de Django cifrados |

Región utilizada: `us-east-1`.

## Seguridad aplicada

- RDS no tiene acceso público.
- PostgreSQL acepta tráfico únicamente desde el grupo de seguridad de EC2.
- El puerto web se limita a las direcciones IP usadas para la demostración.
- EC2 no expone el puerto SSH; la administración se realiza con Session Manager.
- S3 bloquea ACL y políticas públicas.
- Las credenciales no se guardan en GitHub ni dentro de la imagen Docker.
- La aplicación utiliza protección CSRF, cookies HTTP-only y validadores de contraseña de Django.

## Contenedores

Para desarrollo local, `compose.yaml` inicia la aplicación y PostgreSQL. En AWS, EC2 construye `lab6-usuarios:latest` y ejecuta el contenedor con reinicio automático. El script `scripts/user-data.sh` automatiza la instalación y el arranque.

## Validaciones realizadas

- Inicio de sesión administrativo.
- Creación, consulta, actualización y eliminación de un usuario temporal.
- Conexión de Django con RDS PostgreSQL.
- Creación del objeto `profiles/2026/11/avatar-demo.png` mediante el almacenamiento configurado de Django.
- Respuesta satisfactoria de `/health/` dentro y fuera del contenedor.
- Contenedor activo dentro de EC2.

## Evidencias

Las capturas se encuentran en la carpeta `evidencias/` del repositorio y cubren Docker local, RDS, S3, EC2, Docker en EC2, autenticación y operaciones CRUD.

## Costos

RDS y EC2 generan consumo mientras permanezcan activos. Después de presentar el laboratorio, se recomienda eliminar RDS y EC2 o detener temporalmente EC2 si se desea conservar la demostración.
