# Gestión de Vehículos y Rutas con Django

Este proyecto es una aplicación Django para la gestión de vehículos, que utiliza Docker para facilitar su despliegue y ejecución. A continuación, encontrarás instrucciones para configurar y ejecutar el contenedor Docker utilizando un script de PowerShell (`start.ps1`), así como detalles sobre las credenciales predeterminadas para el superusuario de Django.

## Requisitos

Para poder ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- **Docker**: Puedes instalar Docker siguiendo las instrucciones oficiales en [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
- **PowerShell**: Este script ha sido diseñado para ejecutarse en Windows PowerShell. Asegúrate de tener PowerShell actualizado.

## Archivos Importantes

- **`start.ps1`**: Script de PowerShell para construir, detener, eliminar y ejecutar el contenedor Docker.
- **`entrypoint.sh`**: Script que se ejecuta al iniciar el contenedor para aplicar migraciones y crear un superusuario si no existe.
- **`Dockerfile`**: Archivo de configuración de Docker para construir la imagen de la aplicación.
- **`requirements.txt`**: Lista de dependencias necesarias para el proyecto Django.

## Instalación y Ejecución con Docker (Recomendado)

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/usuario/repo-gestion-vehiculos.git
```


### 2. Ejecutar el Script "start.ps1"
Para construir la imagen Docker y ejecutar el contenedor, simplemente corre el script de PowerShell:

```bash
.\start.ps1
```

El script se encargará automaticamente de configurar los recursos necesarios para correr la imagen de la aplicación.

### 3. Acceder a la Aplicación
Una vez que el contenedor esté corriendo, puedes acceder a la interfaz de la aplicación Django abriendo tu navegador y visitando:

```bash
http://localhost:8000
```

### 4. Acceder a la API
Una vez que el contenedor esté corriendo, puedes acceder a la documentación de la api abriendo tu navegador y visitando:

```bash
http://localhost:8000/api/swagger/
```


### 5. Acceder al Panel de Administración de Django
Para acceder al panel de administración, visita:

```bash
http://localhost:8000/admin
```
Utiliza las siguientes credenciales predeterminadas para iniciar sesión:

- Usuario: admin
- Contraseña: adminpass

#### Detalles sobre el entrypoint.sh

El archivo entrypoint.sh asegura que cada vez que el contenedor se inicie, se apliquen las migraciones necesarias para la base de datos y se cree un superusuario si no existe uno. El código para la creación del superusuario es el siguiente:



#### Configuración Adicional

- requirements.txt
El archivo requirements.txt contiene todas las dependencias necesarias para el proyecto Django. Asegúrate de mantener este archivo actualizado con cualquier nueva librería que agregues al proyecto. Ejemplo de contenido:





## Instalación Manual (Sin Docker)
Si prefieres ejecutar el proyecto directamente en tu entorno local sin Docker, sigue estos pasos:

### Requisitos
Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu máquina:

- Python 3.9 o superior: Puedes descargar Python desde https://www.python.org/downloads/.
- Virtualenv (opcional pero recomendado): Para crear un entorno virtual y evitar conflictos de dependencias.

### 1. Clonar el Repositorio
Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/usuario/repo-gestion-vehiculos.git
```
### 2. Crear un Entorno Virtual
Es recomendable usar un entorno virtual para manejar las dependencias del proyecto:

#### Crear Entorno Virtual
```bash
python -m venv venv
```

#### Activar el entorno virtual (powershell)
```bash
.\venv\Scripts\activate
```

### 3. Instalar las Dependencias
Una vez que el entorno virtual esté activado, instala las dependencias requeridas desde requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
El proyecto utiliza una base de datos SQLite por defecto, que no requiere configuración adicional. Si prefieres usar una base de datos diferente (como PostgreSQL), asegúrate de actualizar la configuración de la base de datos en settings.py y aplicar las migraciones.

Para configurar la base de datos con los modelos definidos, ejecuta:

```bash
python manage.py migrate
```
### 5. Crear un Superusuario (Administrador)
Para acceder al panel de administración de Django, necesitas crear un superusuario:

```bash
python manage.py createsuperuser
```
Sigue las instrucciones para establecer un nombre de usuario, correo electrónico y contraseña para el superusuario.

### 6. Ejecutar el Servidor de Desarrollo de Django
Una vez que todo esté configurado, puedes iniciar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

El servidor se iniciará en http://localhost:8000 de forma predeterminada. Puedes acceder a la aplicación Django visitando esta URL en tu navegador.

### 7. Acceder a la Aplicación, API y Panel de Administración

Aplicación Web: http://localhost:8000
Documentación de la API (Swagger): http://localhost:8000/api/swagger/
Panel de Administración de Django: http://localhost:8000/admin