# kubectl describe

> A Kubernetes objektumok és erőforrások részleteinek megjelenítése. További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- A névtérben lévő podok részleteinek megjelenítése:

`kubectl describe pods -n {{namespace}}`

- Névtérben lévő csomópontok részleteinek megjelenítése:

`kubectl describe nodes -n {{namespace}}`

- Egy adott pod részleteinek megjelenítése egy névtérben:

`kubectl describe pods {{pod_name}} -n {{namespace}}`

- Egy névtérben lévő konkrét csomópont részleteinek megjelenítése:

`kubectl describe nodes {{node_name}} -n {{namespace}}`

- A YAML manifesztben definiált Kubernetes objektumok részleteinek megjelenítése:

`kubectl describe -f {{path/to/manifest.yaml}}`
