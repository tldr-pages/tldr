# docker image save

> Экспортировать образы Docker в архив.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Сохранить образ, перенаправив `stdout` в архив `.tar`:

`docker {{[save|image save]}} {{образ}}:{{тег}} > {{путь/к/файлу.tar}}`

- Сохранить образ в архив `.tar`:

`docker {{[save|image save]}} {{[-o|--output]}} {{путь/к/файлу.tar}} {{образ}}:{{тег}}`

- Сохранить все теги образа:

`docker {{[save|image save]}} {{[-o|--output]}} {{путь/к/файлу.tar}} {{имя_образа}}`

- Выборочно сохранить определённые теги образа:

`docker {{[save|image save]}} {{[-o|--output]}} {{путь/к/файлу.tar}} {{имя_образа:тег1 имя_образа:тег2 ...}}`
