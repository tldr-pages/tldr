# crictl

> A CRI-kompatibilis konténerfuttató programok parancssorából. További információ: <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

- Az összes kubernetes pod (Ready és NotReady) listázása:

`crictl pods`

- List all containers (Running and Exited):

`crictl ps --all`

- List all images:

`crictl images`

- Adott konténerekről szóló információk nyomtatása:

`crictl inspect {{container_id1 container_id2 ...}}`

- Egy adott héj megnyitása egy futó konténeren belül:

`crictl exec -it {{container_id}} {{sh}}`

- Egy adott kép kihúzása a nyilvántartásból:

`crictl pull {{image:tag}}`

- Egy adott konténer naplóinak kinyomtatása és \[f\]ollow (követése):

`crictl logs -f {{container_id}}`

- Egy vagy több kép eltávolítása:

`crictl rmi {{image_id1 image_id2 ...}}`
