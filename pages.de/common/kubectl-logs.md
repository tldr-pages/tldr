# kubectl logs

> Logs für Container in einem Pod anzeigen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- Logs für einen Einzelcontainer-Pod anzeigen:

`kubectl logs {{pod_name}}`

- Logs für einen bestimmten Container in einem Pod anzeigen:

`kubectl logs --container {{container_name}} {{pod_name}}`

- Logs für alle Container in einem Pod anzeigen:

`kubectl logs --all-containers={{true}} {{pod_name}}`

- Pod-Logs streamen (folgen):

`kubectl logs --follow {{pod_name}}`

- Pod-Logs streamen (folgen) für einen bestimmten Container in einem Pod:

`kubectl logs --follow --container {{container_name}} {{pod_name}}`

- Pod-Logs die neuer einer relativen Zeit sind `10s`, `5m`, or `1h`:

`kubectl logs --since={{relative_time}} {{pod_name}}`

- Die 10 neuesten Logzeilen in einem Pod anzeigen:

`kubectl logs --tail={{10}} {{pod_name}}`
