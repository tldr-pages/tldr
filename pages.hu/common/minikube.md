# minikube

> Eszköz a Kubernetes helyi futtatásához. További információ: <https://github.com/kubernetes/minikube>.

- Indítsa el a fürtöt:

`minikube start`

- Szerezze meg a fürt IP-címét:

`minikube ip`

- Lépjen be a csomópont portján keresztül kitett my_service nevű szolgáltatásba, és kérje le az URL-t:

`minikube service {{my_service}} --url`

- Nyissa meg a Kubernetes műszerfalat egy böngészőben:

`minikube dashboard`

- Állítsa le a futó fürtöt:

`minikube stop`

- Törölje a fürtöt:

`minikube delete`
