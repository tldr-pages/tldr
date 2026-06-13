# kubectl get

> Получать объекты и ресурсы Kubernetes.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/>.

- Получить все пространства имён в текущем кластере:

`kubectl get {{[ns|namespaces]}}`

- Получить узлы в указанном пространстве имён:

`kubectl get {{[no|nodes]}} {{[-n|--namespace]}} {{пространство_имён}}`

- Получить поды в указанном пространстве имён:

`kubectl get {{[po|pods]}} {{[-n|--namespace]}} {{пространство_имён}}`

- Получить развёртывания в указанном пространстве имён:

`kubectl get {{[deploy|deployments]}} {{[-n|--namespace]}} {{пространство_имён}}`

- Получить сервисы в указанном пространстве имён:

`kubectl get {{[svc|services]}} {{[-n|--namespace]}} {{пространство_имён}}`

- Получить другие ресурсы:

`kubectl get {{persistentvolumeclaims|secret|...}}`

- Получить все ресурсы во всех пространствах имён:

`kubectl get all {{[-A|--all-namespaces]}}`

- Получить объекты Kubernetes, определённые в YAML-манифесте:

`kubectl get {{[-f|--filename]}} {{путь/к/манифесту.yaml}}`
