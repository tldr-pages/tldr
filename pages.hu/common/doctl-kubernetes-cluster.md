# doctl kubernetes cluster

> A Kubernetes fürtök kezelése és a fürtökkel kapcsolatos konfigurációs beállítások megtekintése. További információ: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- Kubernetes fürt létrehozása:

`doctl kubernetes cluster create --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{cluster_name}}`

- Az összes Kubernetes fürt listázása:

`doctl kubernetes cluster list`

- A kubeconfig lekérése és mentése:

`doctl kubernetes cluster kubeconfig save {{cluster_name}}`

- Az elérhető frissítések ellenőrzése:

`doctl kubernetes cluster get-upgrades {{cluster_name}}`

- Fürt frissítése egy új Kubernetes verzióra:

`doctl kubernetes cluster upgrade {{cluster_name}}`

- Fürt törlése:

`doctl kubernetes cluster delete {{cluster_name}}`
