# glab pipeline

> Выводить список конвейеров CI/CD GitLab, просматривать и запускать их.
> Больше информации: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/_index.md>.

- Показать статус выполняемого конвейера в текущей ветке:

`glab pipeline status`

- Показать статус выполняемого конвейера в конкретной ветке:

`glab pipeline status --branch {{имя_ветки}}`

- Вывести список конвейеров:

`glab pipeline list`

- Запустить конвейер вручную в текущей ветке:

`glab pipeline run`

- Запустить конвейер вручную в конкретной ветке:

`glab pipeline run --branch {{имя_ветки}}`
