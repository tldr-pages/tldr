# kubectl get

> Obțineți obiecte și resurse Kubernetes.
> Mai multe informaţii: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>

- Obțineți toate spațiile de nume din clusterul curent:

`kubectl get namespaces`

- Obțineți noduri într-un spațiu de nume specificat:

`kubectl get nodes -n {{namespace}}`

- Obțineți păstăi într-un spațiu de nume specificat:

`kubectl get pods -n {{namespace}}`

- Obțineți implementări într-un spațiu de nume specificat:

`kubectl get deployments -n {{namespace}}`

- Obțineți servicii într-un spațiu de nume specificat:

`kubectl get services -n {{namespace}}`

- Obțineți obiecte Kubernetes definite într-un manifest YAML:

`kubectl get -f {{path/to/manifest}}.yaml`
