# kubectl create

> Создавать ресурс из файла или из `stdin`.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/>.

- Создать ресурс, используя файл определения ресурса:

`kubectl create {{[-f|--filename]}} {{путь/к/файлу.yml}}`

- Создать ресурс из `stdin`:

`kubectl create {{[-f|--filename]}} -`

- Создать развёртывание:

`kubectl create {{[deploy|deployment]}} {{имя_развёртывания}} --image {{образ}}`

- Создать развёртывание с репликами:

`kubectl create {{[deploy|deployment]}} {{имя_развёртывания}} --image {{образ}} --replicas {{количество_реплик}}`

- Создать сервис:

`kubectl create {{[svc|service]}} {{тип_сервиса}} {{имя_сервиса}} --tcp {{порт}}:{{целевой_порт}}`

- Создать пространство имён:

`kubectl create {{[ns|namespace]}} {{имя_пространства_имён}}`
