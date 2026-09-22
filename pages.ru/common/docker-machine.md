# docker-machine

> Создавать машины с Docker и управлять ими.
> Больше информации: <https://github.com/docker-archive-public/docker.machine>.

- Вывести список запущенных машин Docker:

`docker-machine ls`

- Создать новую машину Docker с указанным именем:

`docker-machine create {{имя}}`

- Получить статус машины:

`docker-machine status {{имя}}`

- Запустить машину:

`docker-machine start {{имя}}`

- Остановить машину:

`docker-machine stop {{имя}}`

- Показать информацию о машине:

`docker-machine inspect {{имя}}`
