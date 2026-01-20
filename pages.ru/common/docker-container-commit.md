# docker container commit

> Создавать новый образ из изменений контейнера.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Создать образ из конкретного контейнера:

`docker {{[commit|container commit]}} {{контейнер}} {{образ}}:{{тег}}`

- Применить инструкцию `CMD` Dockerfile к созданному образу:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{команда}}" {{контейнер}} {{образ}}:{{тег}}`

- Применить инструкцию `ENV` Dockerfile к созданному образу:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{имя}}={{значение}}" {{контейнер}} {{образ}}:{{тег}}`

- Создать образ с указанием автора в метаданных:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{автор}}" {{контейнер}} {{образ}}:{{тег}}`

- Создать образ с указанием комментария в метаданных:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{комментарий}}" {{контейнер}} {{образ}}:{{тег}}`

- Создать образ без остановки контейнера во время коммита:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{контейнер}} {{образ}}:{{тег}}`

- Показать справку:

`docker {{[commit|container commit]}} --help`
