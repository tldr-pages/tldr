# kubectl

> Parancssori felület a Kubernetes fürtökkel szembeni parancsok futtatásához. Néhány alparancsnak, mint például a `kubectl run`, saját használati dokumentációja van. További információ: [https://kubernetes.io/docs/reference/kubectl/.](https://kubernetes.io/docs/reference/kubectl/)

- Egy erőforrásról szóló információk listázása további részletekkel:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Megadott pod frissítése az 'unhealthy' címkével és az 'true' értékkel:

`kubectl label pods {{name}} unhealthy=true`

- Az összes különböző típusú erőforrás listázása:

`kubectl get all`

- A csomópontok vagy podok erőforrás (CPU/Memória/Tároló) használatának megjelenítése:

`kubectl top {{pod|node}}`

- A master és a fürtszolgáltatások címének kiírása:

`kubectl cluster-info`

- Egy adott mező magyarázatának megjelenítése:

`kubectl explain {{pods.spec.containers}}`

- Egy podban vagy megadott erőforrásban lévő konténer naplóinak kinyomtatása:

`kubectl logs {{pod_name}}`

- Parancs futtatása egy meglévő podban:

`kubectl exec {{pod_name}} -- {{ls /}}`
