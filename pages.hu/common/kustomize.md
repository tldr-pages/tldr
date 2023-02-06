# kustomize

> A Kustomize egy olyan eszköz, amellyel könnyen telepíthetők erőforrások a Kubernetes számára. További információ: <https://github.com/kubernetes-sigs/kustomize>.

- Kustomize fájl létrehozása az erőforrásokkal és a névtérrel:

`kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}`

- Készítsen kustomize fájlt és telepítse a `kubectl` segítségével:

`kustomize build . | kubectl apply -f -`

- Állítson be egy képet a kustomization fájlban:

`kustomize edit set image {{busybox=alpine:3.6}}`

- A kustomization fájlhoz hozzáadandó Kubernetes erőforrások keresése az aktuális könyvtárban:

`kustomize create --autodetect`
