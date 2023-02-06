# kubectl get

> Kubernetes objektumok és erőforrások lekérése. További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Az aktuális fürt összes névterének lekérdezése:

`kubectl get namespaces`

- Egy megadott névtér csomópontjainak lekérdezése:

`kubectl get nodes -n {{namespace}}`

- Podok lekérdezése egy megadott névtérben:

`kubectl get pods -n {{namespace}}`

- Telepítések lekérdezése egy megadott névtérben:

`kubectl get deployments -n {{namespace}}`

- Szolgáltatások lekérdezése egy megadott névtérben:

`kubectl get services -n {{namespace}}`

- Az összes erőforrás lekérdezése egy megadott névtérben:

`kubectl get all -n {{namespace}}`

- A YAML manifesztben definiált Kubernetes objektumok lekérdezése:

`kubectl get -f {{path/to/manifest.yaml}}`
