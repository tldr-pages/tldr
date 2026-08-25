# docker image load

> Carga imágenes de Docker desde archivos o desde `stdin`.
> Más información: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Carga una imagen de Docker desde `stdin`:

`docker < {{ruta/al/archivo_de_imagen.tar}} {{[load|image load]}}`

- Carga una imagen de Docker desde un archivo específico:

`docker {{[load|image load]}} {{[-i|--input]}} {{ruta/al/archivo_de_imagen.tar}}`

- Carga una imagen de Docker desde un archivo específico en modo silencioso:

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{ruta/al/archivo_de_imagen.tar}}`
