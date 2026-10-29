# flux create

> Создавать или обновлять ресурсы Flux.
> Больше информации: <https://fluxcd.io/flux/cmd/flux_create/>.

- Создать источник GitRepository:

`flux create source git {{имя_источника}} --url {{https://github.com/repository}} --branch {{имя_ветки}}`

- Создать ресурс Kustomization для синхронизации каталога из Git-источника:

`flux create kustomization {{имя_kustomization}} --source {{имя_источника}} --path {{путь/к/каталогу}}`

- Создать HelmRelease:

`flux create helmrelease {{имя_релиза}} --chart {{имя_чарта}} --source {{HelmRepository/имя_репозитория}}`

- Создать секрет для аутентификации в Git-репозитории:

`flux create secret git {{имя_секрета}} --url {{https://github.com/repository}} --username "{{имя_пользователя}}" --password "{{пароль}}"`
