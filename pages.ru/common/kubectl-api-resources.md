# kubectl api-resources

> Выводить поддерживаемые API-ресурсы на сервере.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/>.

- Вывести поддерживаемые API-ресурсы:

`kubectl api-resources`

- Вывести поддерживаемые API-ресурсы с подробной информацией:

`kubectl api-resources {{[-o|--output]}} wide`

- Вывести поддерживаемые API-ресурсы, отсортированные по столбцу:

`kubectl api-resources --sort-by {{имя}}`

- Вывести поддерживаемые ресурсы с пространством имён:

`kubectl api-resources --namespaced`

- Вывести поддерживаемые ресурсы без пространства имён:

`kubectl api-resources --namespaced=false`

- Вывести поддерживаемые API-ресурсы с определённой API-группой:

`kubectl api-resources --api-group {{api_группа}}`
