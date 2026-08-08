# minikube

> Запускать Kubernetes локально.
> Больше информации: <https://minikube.sigs.k8s.io/docs/>.

- Запустить кластер:

`minikube start`

- Получить IP-адрес кластера:

`minikube ip`

- Получить URL сервиса с именем `my_service`, доступного через порт узла:

`minikube service {{my_service}} --url`

- Открыть панель управления Kubernetes в браузере:

`minikube dashboard`

- Остановить запущенный кластер:

`minikube stop`

- Удалить кластер:

`minikube delete`

- Подключиться к сервисам типа LoadBalancer:

`minikube tunnel`
