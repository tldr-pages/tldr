# kind

> Instrument pentru rularea clusterelor locale Kubernetes folosind „noduri” container Docker.
> Proiectat pentru testarea Kubernetes în sine, dar poate fi utilizat pentru dezvoltarea locală sau integrarea continuă.
> Mai multe informaţii: <https://github.com/kubernetes-sigs/kind>

- Creați un cluster local Kubernetes:

`kind create cluster --name {{cluster_name}}`

- Ștergeți unul sau mai multe clustere:

`kind delete clusters {{cluster_name}}`

- Obțineți detalii despre clustere, noduri sau kubeconfig:

`kind get {{clusters|nodes|kubeconfig}}`

- Exportați kubeconfig sau jurnalele:

`kind export {{kubeconfig|logs}}`
