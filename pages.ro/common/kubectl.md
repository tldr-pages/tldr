# kubectl

> Interfață linie de comandă pentru executarea comenzilor împotriva clustere Kubernetes.
> A se vedea, de asemenea, `kubectl describe' și alte pagini pentru informații suplimentare.
> Mai multe informaţii: <https://kubernetes.io/docs/reference/kubectl/>

- Listați informații despre o resursă cu mai multe detalii:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Actualizați pod specificat cu eticheta „nesănătoasă” și valoarea „true”:

`kubectl label pods {{name}} unhealthy=true`

- Listează toate resursele cu diferite tipuri:

`kubectl get all`

- Utilizarea resurselor de afișare (CPU/memorie/stocare) a nodurilor sau a păstăilor:

`kubectl top {{pod|node}}`

- Imprimați adresa serviciilor de master și cluster:

`kubectl cluster-info`

- Afișează o explicație a unui anumit câmp:

`kubectl explain {{pods.spec.containers}}`

- Imprimați jurnalele pentru un container într-un pod sau resursă specificată:

`kubectl logs {{pod_name}}`

- Rulați comanda într-un pod existent:

`kubectl exec {{pod_name}} -- {{ls /}}`
