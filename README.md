# Proyecto Final de Programación 4

Este es el proyecto final de la materia Programación 4. A continuación, se explica cómo iniciar el proyecto, configurar la base de datos y otros detalles relevantes.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- pip (el gestor de paquetes de Python)
- MySQL

## Configuración del Entorno

1.  **Clonar el repositorio:**

    ```bash
    git clone [URL del repositorio]
    cd proyectofinalprog4
    ```
2.  **Crear un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate  # En Windows
    ```
3.  **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar las variables de entorno:**

    Crea un archivo `.env` en el directorio `proyectofinalprog4/backend` y añade las siguientes variables:

    ```env
    DATABASE_URL="mysql+pymysql://root:root@localhost:3306/astros"
    SECRET_KEY="e0310e28dcbdbd3c070e36083c30d8f8d514d9f8292eecc5041eedd186901cb3re"
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    # EMAIL_HOST=smtp.gmail.com
    # EMAIL_PORT=465
    # EMAIL_USERNAME=your_email@gmail.com
    # EMAIL_PASSWORD=your_email_password
    ```

    -   `DATABASE_URL`: La URL de la base de datos MySQL. Asegúrate de que la base de datos `astros` exista o crea una nueva.
    -   `SECRET_KEY`: Una clave secreta para la generación de tokens JWT.
    -   `ALGORITHM`: El algoritmo utilizado para la generación de tokens JWT.
    -   `ACCESS_TOKEN_EXPIRE_MINUTES`: El tiempo de expiración de los tokens de acceso en minutos.
    -   Las variables de correo electrónico son opcionales y se pueden descomentar y configurar si se desea utilizar la funcionalidad de envío de correos.

## Configuración de la Base de Datos

1.  Asegúrate de tener MySQL instalado y funcionando.
2.  Crea una base de datos llamada `astros` (o el nombre que hayas configurado en `DATABASE_URL`).
3.  Ejecuta las migraciones para crear las tablas necesarias:

    ```bash
    # Desde el directorio proyectofinalprog4/backend
    python main.py
    ```

## Iniciar el Proyecto

1.  **Backend:**

    ```bash
    # Desde el directorio proyectofinalprog4/backend
    uvicorn main:app --reload
    ```
    Esto iniciará el servidor backend en `http://localhost:8000`.

2.  **Frontend:**

    ```bash
    # Desde el directorio proyectofinalprog4/frontend
    npm install
    npm start
    ```

    Esto iniciará el servidor frontend en `http://localhost:3000`.

## Uso

Una vez que ambos servidores estén en funcionamiento, puedes acceder a la aplicación a través de tu navegador en `http://localhost:3000`.

## Dependencias

Las dependencias del proyecto se encuentran en el archivo `requirements.txt` para el backend y `package.json` para el frontend.

## Notas Adicionales

-   Asegúrate de que la base de datos MySQL esté configurada correctamente y que el usuario tenga los permisos necesarios.
-   Si tienes problemas con las dependencias, asegúrate de que tu entorno virtual esté activado y que estés utilizando la versión correcta de Python.
-   Si tienes problemas con el inicio del proyecto, revisa los logs de la consola para obtener más información.
