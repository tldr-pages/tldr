# minikube

> Instrument pentru a rula Kubernetes local.
> Mai multe informaţii: <https://github.com/kubernetes/minikube>

- Porniţi clusterul:

`minikube start`

- Obțineți adresa IP a clusterului:

`minikube ip`

- Accesați un serviciu numit my_service expus printr-un port nod și obțineți adresa URL:

`minikube service {{my_service}} --url`

- Deschideți tabloul de bord Kubernetes într-un browser:

`minikube dashboard`

- Opriţi clusterul de alergare:

`minikube stop`

- Şterge clusterul:

`minikube delete`
