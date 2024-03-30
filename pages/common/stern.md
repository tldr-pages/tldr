# stern

> Tail multiple pods and containers from Kubernetes.
> More information: <https://github.com/stern/stern>.

- Tail all pods within a current namespace:

`stern .`

- Tail all pods with a specific status:

`stern . --container-state {{running|waiting|terminated}}`

- Tail all pods that matches a given regular expression:

`stern {{pod_query}}`

- Tail matched pods from all namespaces:

`stern {{pod_query}} --all-namespaces`

- Tail matched pods from 15 minutes ago:

`stern {{pod_query}} --since {{15m}}`

- Tail matched pods with a specific label:

`stern {{pod_query}} --selector {{release=canary}}`
