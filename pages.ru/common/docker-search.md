# docker search

> Искать образы Docker на Docker Hub.
> Больше информации: <https://docs.docker.com/reference/cli/docker/search/>.

- Найти образы Docker по имени или ключевому слову:

`docker search {{ключевое_слово}}`

- Найти образы и показать только официальные:

`docker search {{[-f|--filter]}} is-official=true {{ключевое_слово}}`

- Найти образы и показать только автоматические сборки:

`docker search {{[-f|--filter]}} is-automated=true {{ключевое_слово}}`

- Найти образы с минимальным количеством звёзд:

`docker search {{[-f|--filter]}} stars={{число}} {{ключевое_слово}}`

- Ограничить количество результатов:

`docker search --limit {{число}} {{ключевое_слово}}`

- Настроить формат вывода:

`docker search {{[-f|--format]}} "{{.Name}}: {{.Description}}" {{ключевое_слово}}`
