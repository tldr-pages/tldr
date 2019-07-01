# stern

> Tail multiple pods and containers from Kubernetes.
> More information: <https://github.com/wercker/stern/>.

- Tail all pods within a current namespace:

`stern .`

- Tail all pods with status waiting:

`stern . --container-state {{waiting}}`

- Tail all pods that matches regular expression:

`stern {{pod_query}}`

- Tail matched pods from all namespaces:

`stern {{pod_query}} --all-namespaces`

- Tail matched pods from 15m ago:

`stern {{pod_query}} --since {{15m}}`

- Tail matched pods with a specific label:

`stern {{pod_query}} --selector {{release=canary}}`
