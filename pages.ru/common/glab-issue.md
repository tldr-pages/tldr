# glab issue

> Управлять задачами GitLab.
> Больше информации: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/issue/_index.md>.

- Показать конкретную задачу:

`glab issue view {{номер_задачи}}`

- Открыть конкретную задачу в браузере по умолчанию:

`glab issue view {{номер_задачи}} {{[-w|--web]}}`

- Создать новую задачу в браузере по умолчанию:

`glab issue create --web`

- Вывести список последних 10 задач с меткой `bug`:

`glab issue list {{[-P|--per-page]}} {{10}} {{[-l|--label]}} "{{bug}}"`

- Вывести список закрытых задач, созданных конкретным пользователем:

`glab issue list {{[-c|--closed]}} --author {{имя_пользователя}}`

- Переоткрыть конкретную задачу:

`glab issue reopen {{номер_задачи}}`
