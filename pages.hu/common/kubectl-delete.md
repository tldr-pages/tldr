# kubectl delete

> Kubernetes erőforrások törlése. További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Egy adott pod törlése:

`kubectl delete pod {{pod_name}}`

- Egy adott telepítés törlése:

`kubectl delete deployment {{deployment_name}}`

- Egy adott csomópont törlése:

`kubectl delete node {{node_name}}`

- Az összes pod törlése egy megadott névtérben:

`kubectl delete pods --all --namespace {{namespace}}`

- Az összes telepítés és szolgáltatás törlése egy megadott névtérben:

`kubectl delete deployments,services --all --namespace {{namespace}}`

- Az összes csomópont törlése:

`kubectl delete nodes --all`

- YAML manifesztben meghatározott erőforrások törlése:

`kubectl delete --filename {{path/to/manifest.yaml}}`
