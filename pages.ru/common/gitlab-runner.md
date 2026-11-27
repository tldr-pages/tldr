# gitlab-runner

> Управлять раннерами GitLab.
> Больше информации: <https://docs.gitlab.com/runner/>.

- Зарегистрировать раннер:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{токен}} --name {{имя}}`

- Зарегистрировать раннер с исполнителем Docker:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{токен}} --name {{имя}} --executor {{docker}}`

- Отменить регистрацию раннера:

`sudo gitlab-runner unregister --name {{имя}}`

- Показать статус сервиса раннера:

`sudo gitlab-runner status`

- Перезапустить сервис раннера:

`sudo gitlab-runner restart`

- Проверить, могут ли зарегистрированные раннеры подключиться к GitLab:

`sudo gitlab-runner verify`
