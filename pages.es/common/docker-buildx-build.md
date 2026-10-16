# docker buildx build

> Compila una imagen a partir de un Dockerfile utilizando el motor BuildKit.
> Más información: <https://docs.docker.com/reference/cli/docker/buildx/build>.

- Compila una imagen a partir del Dockerfile del directorio actual:

`docker buildx build .`

- Compila una imagen y la etiqueta:

`docker buildx build {{[-t|--tag]}} {{image:tag}} .`

- Compila una imagen utilizando un Dockerfile específico:

`docker buildx build {{[-f|--file]}} {{ruta/a/Dockerfile}} .`

- Compila una imagen pasando variables de compilación:

`docker buildx build --build-arg {{HTTP_PROXY=http://proxy.example.com}} --build-arg {{VERSION=1.0}} .`

- Compila una imagen sin utilizar la caché de compilación:

`docker buildx build --no-cache .`

- Compila una imagen y la carga en `docker images`:

`docker buildx build --load {{[-t|--tag]}} {{image:tag}} .`

- Compila para varias plataformas y la envsubirla a un registro:

`docker buildx build --platform {{linux/amd64,linux/arm64}} --push {{[-t|--tag]}} {{registry.example.com/image:tag}} .`

- Compilar una etapa específica a partir de un Dockerfile de varias etapas:

`docker buildx build --target {{nombre_etapa}} {{[-t|--tag]}} {{image:tag}} .`
