# kubectl cluster-info

> Отображать информацию об адресах мастера Kubernetes и служб в кластере.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/>.

- Показать базовую информацию о кластере:

`kubectl cluster-info`

- Сделать дамп текущего состояния кластера в `stdout` (для отладки):

`kubectl cluster-info dump`

- Сделать дамп состояния кластера в каталог:

`kubectl cluster-info dump --output-directory {{путь/к/каталогу}}`

- Использовать определённый контекст kubeconfig:

`kubectl cluster-info --context {{имя_контекста}}`
