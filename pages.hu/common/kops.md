# kops

> A Kubernetes fürtök létrehozása, megsemmisítése, frissítése és karbantartása a parancssorból. További információ: <https://github.com/kubernetes/kops/>.

- Fürt létrehozása a konfigurációs specifikációból:

`kops create cluster -f {{cluster_name.yaml}}`

- Hozzon létre egy új ssh nyilvános kulcsot:

`kops create secret sshpublickey {{key_name}} -i {{~/.ssh/id_rsa.pub}}`

- Exportálja a fürtkonfigurációt a `~/.kube/config` fájlba:

`kops export kubecfg {{cluster_name}}`

- A fürtkonfiguráció YAML formátumban történő lekérdezése:

`kops get cluster {{cluster_name}} -o yaml`

- Egy fürt törlése:

`kops delete cluster {{cluster_name}} --yes`
