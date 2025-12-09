# podman build

> Herramienta que no corre como servicio (daemon) para construir imágenes de contenedores.
> Podman proporciona una línea de comando comparable con Docker-CLI. En pocas palabras: `alias docker=podman`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Crea una imagen usando un `Dockerfile` o `Containerfile` en el directorio especificado:

`podman build {{ruta/al/directorio}}`

- Crea una imagen con una etiqueta especificada:

`podman build --tag {{nombre_de_la_imagen:version}} {{ruta/al/directorio}}`

- Crea una imagen de un archivo no estándar:

`podman build --file {{Archivo_contenedor.different}} .`

- Crea una imagen sin usar ninguna imagen previamente almacenada en caché:

`podman build --no-cache {{ruta/al/directorio}}`

- Crea una imagen suprimiendo cualquier mensaje informativo (output):

`podman build --quiet {{ruta/al/directorio}}`
