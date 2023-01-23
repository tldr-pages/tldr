# k3d

> Wrapper CLI a k3s klaszterek egyszerű létrehozásához a Dockeren belül. További információ [: https://k3d.io](https://k3d.io).

- Hozzon létre egy fürtöt:

`k3d cluster create {{cluster_name}}`

- Klaszter törlése:

`k3d cluster delete {{cluster_name}}`

- Új konténeres k3s csomópont létrehozása:

`k3d node create {{node_name}}`

- Kép importálása Dockerből egy k3s fürtbe:

`k3d image import {{image_name}} --cluster {{cluster_name}}`

- Új registry létrehozása:

`k3d registry create {{registry_name}}`
