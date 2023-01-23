# kubeadm

> Parancssori felület a Kubernetes fürtök létrehozásához és kezeléséhez. További információ: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Hozzon létre egy Kubernetes mester csomópontot:

`kubeadm init`

- Egy Kubernetes-munkáscsomópont bootstrapelése és csatlakoztatása egy fürthöz:

`kubeadm join --token {{token}}`

- Hozzon létre egy új bootstrap tokent 12 órás TTL-sel:

`kubeadm token create --ttl {{12h0m0s}}`

- Ellenőrizze, hogy a Kubernetes fürt frissíthető-e és milyen verziók állnak rendelkezésre:

`kubeadm upgrade plan`

- A Kubernetes fürt frissítése egy megadott verzióra:

`kubeadm upgrade apply {{version}}`

- A fürt konfigurációját tartalmazó kubeadm ConfigMap megtekintése:

`kubeadm config view`

- A 'kubeadm init' vagy 'kubeadm join' által a gazdán végrehajtott változtatások visszavonása:

`kubeadm reset`
