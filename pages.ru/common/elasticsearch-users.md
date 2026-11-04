# elasticsearch-users

> Управлять пользователями нативной области в Elasticsearch, включая создание, обновление и удаление пользователей.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/users-command>.

- Добавить нового пользователя в интерактивном режиме (будет запрошен пароль):

`elasticsearch-users useradd {{имя_пользователя}}`

- Добавить нового пользователя и указать роли:

`elasticsearch-users useradd {{имя_пользователя}} -r {{роль1,роль2}}`

- Изменить пароль существующего пользователя:

`elasticsearch-users passwd {{имя_пользователя}}`

- Удалить пользователя:

`elasticsearch-users userdel {{имя_пользователя}}`

- Вывести список всех пользователей в нативной области:

`elasticsearch-users list`
