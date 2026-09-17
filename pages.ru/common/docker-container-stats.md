# docker container stats

> Отображать статистику использования ресурсов контейнеров в реальном времени.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- Отобразить статистику всех запущенных контейнеров в реальном времени:

`docker {{[stats|container stats]}}`

- Отобразить статистику для одного или нескольких контейнеров в реальном времени:

`docker {{[stats|container stats]}} {{контейнер1 контейнер2 ...}}`

- Изменить формат вывода для отображения процента загрузки процессора:

`docker {{[stats|container stats]}} --format "{{.Name}}:\t{{.CPUPerc}}"`

- Отобразить статистику для всех контейнеров (запущенных и остановленных):

`docker {{[stats|container stats]}} {{[-a|--all]}}`

- Отключить потоковый вывод и показать только текущую статистику:

`docker {{[stats|container stats]}} --no-stream`
