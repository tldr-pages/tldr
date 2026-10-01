# docker buildx build

> Собирать образ из Dockerfile с использованием движка BuildKit.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/build>.

- Собрать образ из Dockerfile в текущем каталоге:

`docker buildx build .`

- Собрать образ и присвоить ему тег:

`docker buildx build {{[-t|--tag]}} {{образ:тег}} .`

- Собрать образ с использованием определённого Dockerfile:

`docker buildx build {{[-f|--file]}} {{путь/к/Dockerfile}} .`

- Собрать образ с передачей переменных времени сборки:

`docker buildx build --build-arg {{HTTP_PROXY=http://proxy.example.com}} --build-arg {{VERSION=1.0}} .`

- Собрать образ без использования кэша сборки:

`docker buildx build --no-cache .`

- Собрать образ и загрузить его в `docker images`:

`docker buildx build --load {{[-t|--tag]}} {{образ:тег}} .`

- Собрать для нескольких платформ и отправить в реестр:

`docker buildx build --platform {{linux/amd64,linux/arm64}} --push {{[-t|--tag]}} {{registry.example.com/образ:тег}} .`

- Собрать определённый этап из многоэтапного Dockerfile:

`docker buildx build --target {{имя_этапа}} {{[-t|--tag]}} {{образ:тег}} .`
