# glab release

> Управлять релизами GitLab.
> Больше информации: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/release/_index.md>.

- Вывести список релизов в репозитории GitLab (не более 30):

`glab release list`

- Показать информацию о конкретном релизе:

`glab release view {{тег}}`

- Создать новый релиз:

`glab release create {{тег}}`

- Удалить конкретный релиз:

`glab release delete {{тег}}`

- Скачать файлы конкретного релиза:

`glab release download {{тег}}`

- Загрузить файлы в конкретный релиз:

`glab release upload {{тег}} {{путь/к/файлу1 путь/к/файлу2 ...}}`
