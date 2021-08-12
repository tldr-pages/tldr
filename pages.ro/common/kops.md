# kops

> Creați, distrugeți, faceți upgrade și mențineți clustere Kubernetes din linia de comandă.
> Mai multe informaţii: <https://github.com/kubernetes/kops/>

- Creați un cluster din specificația de configurare:

`kops create cluster -f {{cluster_name.yaml}}`

- Creați o nouă cheie publică ssh:

`kops create secret sshpublickey {{key_name}} -i {{~/.ssh/id_rsa.pub}}`

- Exportați configurația clusterului în fișierul `~/.kube/config`:

`kops export kubecfg {{cluster_name}}`

- Obțineți configurația clusterului ca yaml:

`kops get cluster {{cluster_name}} -o yaml`

- Şterge un cluster:

`kops delete cluster {{cluster_name}} --yes`
