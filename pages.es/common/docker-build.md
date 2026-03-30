# docker build

> Construye una imagen a partir de un Dockerfile.
> Más información: <https://docs.docker.com/reference/cli/docker/buildx/build/>.

- Construye una imagen Docker usando el Dockerfile del directorio actual:

`docker build .`

- Construye una imagen Docker desde un Dockerfile en una URL específica:

`docker build {{github.com/creack/docker-firefox}}`

- Construye una imagen Docker y la etiqueta:

`docker build {{[-t|--tag]}} {{nombre:etiqueta}} .`

- Construye una imagen Docker sin contexto de compilación:

`docker < {{Dockerfile}} build {{[-t|--tag]}} {{nombre:etiqueta}} -`

- No usa la caché al construir la imagen:

`docker build --no-cache {{[-t|--tag]}} {{nombre:etiqueta}} .`

- Construye una imagen Docker usando un Dockerfile específico:

`docker build {{[-f|--file]}} {{Dockerfile}} .`

- Construye con variables personalizadas en tiempo de compilación:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
