# Guion del video de demostración

Duración objetivo: 2 minutos

## Preparación antes de grabar

1. Abre Amazon RDS en la lista de bases de datos.
2. Abre Amazon S3 dentro de `profiles/2026/11/`.
3. Abre Amazon EC2 en la lista de instancias.
4. Abre Session Manager y deja ejecutado `sudo docker ps`.
5. Abre `http://100.30.202.40:8000/admin/` y deja preparada la pantalla de acceso.
6. Ten disponible una imagen pequeña para crear un usuario durante la demostración.
7. No muestres contraseñas, parámetros cifrados ni archivos `.env`.

## 0:00 a 0:10 Presentación

**Mostrar:** título o README del repositorio.

**Decir:**

> Soy Miguel Angel Champi Hinojosa. Esta es la solución de la pregunta 1 del Laboratorio 6. La aplicación administra usuarios y está desplegada en AWS con EC2, RDS PostgreSQL, S3 y Docker.

## 0:10 a 0:25 Servicios AWS

**Mostrar:** RDS y cambiar rápidamente a S3.

**Decir:**

> La base `lab6-postgres` está disponible en Amazon RDS y no tiene acceso público. Las imágenes de perfil se almacenan de forma privada en este bucket S3; aquí se observa un objeto dentro de la carpeta `profiles`.

## 0:25 a 0:38 EC2 y Docker

**Mostrar:** la instancia `lab6-usuarios-ec2` en ejecución y la terminal de Session Manager con `docker ps`.

**Decir:**

> La aplicación se ejecuta en esta instancia EC2 `t3.micro`. No se utiliza SSH público; la administración se realiza con Session Manager. El comando `docker ps` confirma que el contenedor está activo y publica el puerto 8000.

## 0:38 a 0:52 Autenticación

**Mostrar:** la pantalla de acceso y luego iniciar sesión.

**Decir:**

> El acceso al panel está protegido y requiere una cuenta administrativa. Ingreso con el perfil administrador para gestionar los usuarios.

Evita que la contraseña sea visible durante la grabación.

## 0:52 a 1:12 Consulta y creación

**Mostrar:** lista de usuarios, pulsar `Añadir usuario`, completar nombre, contraseña, teléfono, rol y foto, y guardar.

**Decir:**

> Esta es la consulta de usuarios registrados. Ahora creo un usuario nuevo, asigno sus datos básicos, selecciono su rol y adjunto una foto de perfil. Al guardar, los datos se registran en RDS y la imagen se envía a S3.

## 1:12 a 1:32 Actualización

**Mostrar:** abrir el usuario recién creado, cambiar teléfono o rol y guardar.

**Decir:**

> Para demostrar la actualización, modifico el teléfono o el rol y guardo los cambios. El sistema confirma que el usuario fue actualizado correctamente.

## 1:32 a 1:47 Eliminación

**Mostrar:** pulsar `Eliminar`, confirmar y regresar a la lista.

**Decir:**

> Finalmente, elimino el usuario de prueba. La aplicación solicita confirmación y luego lo retira de la base de datos.

## 1:47 a 2:00 Cierre

**Mostrar:** lista final de usuarios o endpoint `/health/`.

**Decir:**

> Con esto se demuestra autenticación, CRUD completo, base de datos PostgreSQL en RDS, imágenes en S3 y despliegue mediante Docker en EC2. El código, README, documentación técnica y evidencias se encuentran en el repositorio público.

## Lista de control

- El video dura aproximadamente 2 minutos y nunca supera 5 minutos.
- Se muestra RDS disponible.
- Se muestra el objeto de perfil en S3.
- Se muestra EC2 en ejecución.
- Se muestra el contenedor con `docker ps`.
- Se muestra inicio de sesión administrativo.
- Se demuestra crear, consultar, actualizar y eliminar.
- No se muestra ninguna contraseña o secreto.
