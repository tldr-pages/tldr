# kubectl run

> Podok futtatása a Kubernetesben. Megadja a pod generátort, hogy elkerülje a deprecációs hibát egyes K8S verziókban. További információ: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Futtasson egy nginx podot és tegye ki a 80-as portot:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --port 80`

- Futtasson egy nginx podot, a TEST_VAR környezeti változó beállításával:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --env="TEST_VAR=testing"`

- Az nginx konténer létrehozásához szükséges API-hívások megjelenítése:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run`

- Egy Ubuntu pod futtatása interaktívan, soha ne indítsa újra, és távolítsa el, amikor kilép:

`kubectl run --generator=run-pod/v1 -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Egy Ubuntu pod futtatása, az alapértelmezett parancs echo-val való felülírása és egyéni argumentumok megadása:

`kubectl run --generator=run-pod/v1 temp-ubuntu --image=ubuntu:20.04 --command -- echo arg1 arg2 arg3`
