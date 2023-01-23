# kubectl rollout

> A Kubernetes-erőforrás bevezetésének kezelése (telepítések, daemonsetek és állapotkészletek). További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- Egy erőforrás gördülő újraindításának elindítása:

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- Figyelje egy erőforrás gördülő frissítési állapotát:

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- Egy erőforrás visszaállítása az előző revízióra:

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- Egy erőforrás gördülési előzményeinek megtekintése:

`kubectl rollout history {{resource_type}}/{{resource_name}}`
