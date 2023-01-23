# stern

> Több pod és konténer követése a Kubernetesből. További információ: <https://github.com/wercker/stern/>.

- Az aktuális névtérben lévő összes podot követése:

`stern .`

- Tail az összes podot egy adott státuszban:

`stern . --container-state {{running|waiting|terminated}}`

- Tail minden pod, amely megfelel egy adott reguláris kifejezésnek:

`stern {{pod_query}}`

- Az összes névtérből származó, egyező podok törlése:

`stern {{pod_query}} --all-namespaces`

- Tail matched pods from 15 minutes ago:

`stern {{pod_query}} --since {{15m}}`

- Tail matched pods with a specific label:

`stern {{pod_query}} --selector {{release=canary}}`
