# Laboratorio 6 Administración de usuarios en AWS

Aplicación web desarrollada para la pregunta 1 del Laboratorio 6 de Introducción a Cognitive Computing.

**Estudiante:** Miguel Angel Champi Hinojosa  
**Código:** 202110072  
**Docente:** Farfán Madariaga, Jaime Moshe

## Funciones implementadas

- Acceso autenticado para el administrador.
- Creación, consulta, actualización y eliminación de usuarios.
- Perfil con teléfono, rol, estado y foto.
- PostgreSQL local para pruebas y Amazon RDS PostgreSQL en producción.
- Almacenamiento privado de fotos en Amazon S3 mediante enlaces temporales.
- Contenedor Docker ejecutable localmente y en Amazon EC2.
- Credenciales configuradas solo mediante variables de entorno o rol IAM.
- Endpoint de verificación en `/health/`.

## Ejecución local

1. Copiar `.env.example` como `.env` y cambiar las contraseñas.
2. Ejecutar `docker compose up --build -d`.
3. Abrir `http://localhost:8010/admin/`.
4. Comprobar los contenedores con `docker compose ps`.

## Arquitectura de despliegue

El navegador accede a la aplicación Django ejecutada en un contenedor Docker dentro de EC2. Django guarda los datos en Amazon RDS PostgreSQL y las fotos privadas en Amazon S3. La instancia EC2 obtiene acceso a S3 mediante un rol IAM, sin claves permanentes dentro del repositorio.

## Variables para AWS

En EC2, `.env` debe usar el endpoint privado de RDS en `POSTGRES_HOST`, la IP pública de EC2 en `DJANGO_ALLOWED_HOSTS` y el bucket creado en `AWS_STORAGE_BUCKET_NAME`. Nunca se debe subir `.env` al repositorio.

## Evidencias mínimas previstas

1. Inicio de sesión y lista de usuarios.
2. Usuario creado o actualizado con foto.
3. Objeto de la foto dentro del bucket S3.
4. Instancia RDS disponible.
5. Instancia EC2 en ejecución y regla del puerto de la aplicación.
6. Contenedor Docker activo en EC2.
7. Aplicación funcionando desde la IP pública de EC2.

El video demostrativo se preparará después de completar y verificar las capturas.
