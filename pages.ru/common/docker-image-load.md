# docker image load

> Загружать образы Docker из файлов или `stdin`.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Загрузить образ Docker из `stdin`:

`docker < {{путь/к/файлу_образа.tar}} {{[load|image load]}}`

- Загрузить образ Docker из определённого файла:

`docker {{[load|image load]}} {{[-i|--input]}} {{путь/к/файлу_образа.tar}}`

- Загрузить образ Docker из определённого файла в тихом режиме:

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{путь/к/файлу_образа.tar}}`
