# docker

> Управление контейнерами и образами Docker.
> Некоторые подкоманды, такие как `run`, имеют собственную документацию по использованию.
> Больше информации: https://docs.docker.com/reference/cli/docker/.

- Список всех контейнеров Docker (запущенных и остановленных):

`docker ps --all`

- Запустить контейнера из образа с заданным именем:

`docker run --name container_name image`

- Запустить или остановить существующий контейнер:

`docker start|stop container_name`

- Загрузить образ из репозитория Docker:

`docker pull image`

- Показать список уже загруженных образов:

`docker images`

- Запустить интерактивный [i] телетайп [t] с командной оболочкой (sh) внутри запущенного контейнера:

`docker exec -it container_name sh`

- Удалить остановленный контейнер:

`docker rm container_name`

- Получить и следить за логами контейнера:

`docker logs -f container_name`
