# Tarea del Módulo 1: Docker y SQL

En esta tarea, prepararemos el entorno y practicaremos Docker y SQL.

Al entregar tu tarea, también deberás incluir un enlace a tu repositorio de GitHub u otro sitio público de alojamiento de código.

Este repositorio debe contener el código para resolver la tarea.

Si tu solución contiene comandos SQL o de shell, pero no código (por ejemplo, archivos de Python), inclúyelos directamente en el archivo README de tu repositorio.
_______

## Configuración

Este proyecto está configurado para ejecutarse en Firebase Studio. La configuración del proyecto se define en el archivo `pyproject.toml` y es la siguiente:

Nombre del proyecto: mod1_dockerysql
Versión:0.1.0
Descripción:Este es un proyecto de inicio para desarrollar aplicaciones en Python.
Versión de Python requerida: >=3.11
Dependencias: ["pandas", "sqlalchemy", "psycopg2", "pyarrow"]

## Pregunta 1. Comprensión de las imágenes de Docker
Ejecuta Docker con la imagen `python:3.13`. Usa un punto de entrada `bash` para interactuar con el contenedor.

¿Cuál es la versión de `pip` en la imagen?

Ejecutar comando en terminal bash : 
docker run --rm --entrypoint bash python:3.13 -c "pip --version”

Respuesta :
25.3

## Pregunta 2. Comprensión de la red Docker y docker-compose

Hostname: db (o postgres)
Port: 5432
Nota: La opción db:5432 es la más estándar en Docker Compose, ya que el nombre del servicio es el identificador principal. Sin embargo, debido a que configuraste container_name: postgres, postgres:5432 también es técnicamente correcto y funcional.


