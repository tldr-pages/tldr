# glab auth

> Аутентифицироваться на хосте GitLab.
> Больше информации: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/auth/_index.md>.

- Войти в интерактивном режиме:

`glab auth login`

- Войти с использованием токена:

`glab auth login {{[-t|--token]}} {{токен}}`

- Проверить статус аутентификации:

`glab auth status`

- Войти на конкретный экземпляр GitLab:

`glab auth login {{[-h|--hostname]}} {{gitlab.example.com}}`
