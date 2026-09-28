# docker inspect

> Возвращать низкоуровневую информацию об объектах Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Показать информацию о контейнере, образе или томе по имени или идентификатору:

`docker inspect {{контейнер|образ|идентификатор}}`

- Показать IP-адрес контейнера:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{контейнер}}`

- Показать путь к файлу журнала контейнера:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{контейнер}}`

- Показать имя образа контейнера:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{контейнер}}`

- Показать информацию о конфигурации в формате JSON:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{контейнер}}`

- Показать все привязки портов:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{контейнер}}`

- Показать справку:

`docker inspect`
