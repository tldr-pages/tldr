# kubectl

> Выполнять команды в кластерах Kubernetes.
> Некоторые подкоманды, такие как `run`, имеют собственную документацию.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/>.

- Вывести подробную информацию о ресурсе:

`kubectl get {{pods|service|deployment|ingress|...}} {{[-o|--output]}} wide`

- Присвоить указанному поду метку `unhealthy` со значением `true`:

`kubectl label pods {{имя}} unhealthy=true`

- Вывести список всех ресурсов:

`kubectl get all`

- Показать использование ресурсов (CPU/память/хранилище) узлами или подами:

`kubectl top {{pods|nodes}}`

- Показать адреса мастера и служб кластера:

`kubectl cluster-info`

- Показать описание определённого поля:

`kubectl explain {{pods.spec.containers}}`

- Вывести логи контейнера в поде:

`kubectl logs {{имя_пода}}`

- Выполнить команду в существующем поде:

`kubectl exec {{имя_пода}} -- {{ls /}}`
