# kubectl delete

> Удалять ресурсы Kubernetes.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete/>.

- Удалить конкретный под:

`kubectl delete {{[po|pods]}} {{имя_пода}}`

- Удалить конкретное развёртывание:

`kubectl delete {{[deploy|deployments]}} {{имя_развёртывания}}`

- Удалить конкретный узел:

`kubectl delete {{[no|nodes]}} {{имя_узла}}`

- Удалить все поды в указанном пространстве имён:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{пространство_имён}}`

- Удалить все развёртывания и сервисы в указанном пространстве имён:

`kubectl delete {{[deploy|deployments]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{пространство_имён}}`

- Удалить все узлы:

`kubectl delete {{[no|nodes]}} --all`

- Удалить ресурсы, определённые в YAML-манифесте:

`kubectl delete {{[-f|--filename]}} {{путь/к/манифесту.yaml}}`
