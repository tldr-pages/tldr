# docker image pull

> Скачивать образы Docker из реестра.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Скачать определённый образ Docker:

`docker {{[pull|image pull]}} {{образ}}:{{тег}}`

- Скачать определённый образ Docker в тихом режиме:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{образ}}:{{тег}}`

- Скачать все теги определённого образа Docker:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{образ}}`

- Скачать образ Docker для определённой платформы:

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{образ}}:{{тег}}`

- Показать справку:

`docker {{[pull|image pull]}} --help`
