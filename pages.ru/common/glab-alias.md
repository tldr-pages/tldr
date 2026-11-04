# glab alias

> Управлять псевдонимами команд GitLab CLI.
> Больше информации: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/alias/_index.md>.

- Вывести список всех псевдонимов, настроенных для `glab`:

`glab alias list`

- Создать псевдоним подкоманды `glab`:

`glab alias set {{mrv}} '{{mr view}}'`

- Задать команду оболочки как подкоманду `glab`:

`glab alias set {{[-s|--shell]}} {{имя_псевдонима}} {{команда}}`

- Удалить сокращение команды:

`glab alias delete {{имя_псевдонима}}`

- Показать справку по подкоманде:

`glab alias`
