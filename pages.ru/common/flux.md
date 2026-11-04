# flux

> Решение для непрерывной и прогрессивной доставки в Kubernetes.
> Больше информации: <https://fluxcd.io/flux/cmd/>.

- Проверить, выполнены ли предварительные требования Flux в кластере:

`flux check --pre`

- Выполнить начальную установку Flux в кластере Kubernetes:

`flux bootstrap {{github|gitlab}} --owner {{owner}} --repository {{repository}} --path {{путь/к/каталогу_кластера}}`

- Создать новый источник GitRepository:

`flux create source git {{имя_источника}} --url {{https://github.com/repository}} --branch {{имя_ветки}}`

- Показать все пользовательские ресурсы Flux:

`flux get all`

- Запустить согласование для конкретной Kustomization и применить изменения из источника:

`flux reconcile kustomization {{имя}} --with-source`

- Приостановить согласование для Kustomization:

`flux suspend kustomization {{имя}}`

- Возобновить согласование для Kustomization:

`flux resume kustomization {{имя}}`

- Показать справку по конкретной подкоманде:

`flux {{подкоманда}} --help`
