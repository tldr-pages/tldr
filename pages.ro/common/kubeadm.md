# kubeadm

> Interfață linie de comandă pentru crearea și gestionarea clustere Kubernetes.
> Mai multe informaţii: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>

- Creați un nod principal Kubernetes:

`kubeadm init`

- Bootstrap un nod de lucrător Kubernetes și se alăture la un cluster:

`kubeadm join --token {{token}}`

- Creați un nou token bootstrap cu un TTL de 12 ore:

`kubeadm token create --ttl {{12h0m0s}}`

- Verificați dacă clusterul Kubernetes este upgradabil și ce versiuni sunt disponibile:

`kubeadm upgrade plan`

- Upgrade Kubernetes cluster la o versiune specificată:

`kubeadm upgrade apply {{version}}`

- Vizualizați Kubeadm ConfigMap care conține configurația clusterului:

`kubeadm config view`

- Reveniți modificările aduse gazdei prin 'kubeadm init' sau 'kubeadm join':

`kubeadm reset`
