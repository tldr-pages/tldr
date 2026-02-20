# hf

> Interactúa con Hugging Face Hub.
> Inicia sesión, gestiona la caché local, carga o descarga archivos.
> Más información: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Inicia sesión en Hugging Face Hub:

`hf login`

- Muestra el nombre del usuario conectado:

`hf whoami`

- Cierra sesión:

`hf logout`

- Genera información sobre el entorno:

`hf env`

- Descarga archivos de un repositorio e imprime la ruta (omite los nombres de archivo para descargar todo el repositorio):

`hf download --repo-type {{repo_type}} {{repo_id}} {{nombre_archivo1 nombre_archivo2 ...}}`

- Sube una carpeta entera o un archivo a Hugging Face:

`hf upload --repo-type {{repo_type}} {{repo_id}} {{ruta/al/archivo_de_repositorio_o_directorio_de_repositorio}} {{ruta/al/archivo_de repositorio_o_directorio}}`

- Escanea la caché para ver los repositorios descargados y su uso de disco:

`hf scan-cache`

- Elimina la caché de forma interactiva:

`hf delete-cache`
