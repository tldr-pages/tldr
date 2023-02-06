# kubectl logs

> A podban lévő konténerek naplóinak megjelenítése. További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- Egyetlen konténer pod naplóinak megjelenítése:

`kubectl logs {{pod_name}}`

- Naplók megjelenítése egy podban lévő megadott konténerhez:

`kubectl logs --container {{container_name}} {{pod_name}}`

- Naplók megjelenítése egy pod összes konténeréhez:

`kubectl logs --all-containers={{true}} {{pod_name}}`

- Pod-naplók streamelése:

`kubectl logs --follow {{pod_name}}`

- Stream logs for a meghatározott konténer egy podban:

`kubectl logs --follow --container {{container_name}} {{pod_name}}`

- Egy relatív időpontnál újabb pod-naplók megjelenítése, például `10s`, `5m` vagy `1h`:

`kubectl logs --since={{relative_time}} {{pod_name}}`

- A pod 10 legfrissebb naplójának megjelenítése:

`kubectl logs --tail={{10}} {{pod_name}}`
