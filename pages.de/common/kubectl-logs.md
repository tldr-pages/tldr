# kubectl logs

> Logs für Container in einem Pod anzeigen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- Zeige Logs für einen Einzelcontainer-Pod an:

`kubectl logs {{pod_name}}`

- Zeige Logs für einen bestimmten Container in einem Pod an:

`kubectl logs --container {{container_name}} {{pod_name}}`

- Zeige Logs für alle Container in einem Pod an:

`kubectl logs --all-containers={{true}} {{pod_name}}`

- Folge den Pod-Logs (stream):

`kubectl logs --follow {{pod_name}}`

- Folge den Pod-Logs (stream) für einen bestimmten Container in einem Pod:

`kubectl logs --follow --container {{container_name}} {{pod_name}}`

- Zeige Pod-Logs die neuer einer relativen Zeit sind `10s`, `5m`, or `1h`:

`kubectl logs --since={{relative_time}} {{pod_name}}`

- Zeige die 10 neuesten Logzeilen in einem Pod:

`kubectl logs --tail={{10}} {{pod_name}}`
