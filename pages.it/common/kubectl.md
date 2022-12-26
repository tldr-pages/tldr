# kubectl

> Interfaccia interattiva da linea di comando per eseguire comandi sui clusters Kubernetes.
> Alcuni comandi aggiuntivi, come `kubectl run`, hanno la propria documentazione..
> Maggiori informazioni: <https://kubernetes.io/docs/reference/kubectl/>.

- Elenca le informazioni su una risorsa in maniera dettagliata:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Aggiorna il pod specificato con l'etichetta 'unhealthy' e il valore 'true':

`kubectl label pods {{nome}} unhealthy=true`

- Elenca tutte le risorse:

`kubectl get all`

- Mostra l'utilizzo delle risorse (CPU/Memory/Storage) di nodi o pods:

`kubectl top {{pod|nodo}}`

- Mostra l'indirizzo del master e i servizi del cluster:

`kubectl cluster-info`

- Mostra la spiegazione di un campo specifico:

`kubectl explain {{pods.spec.containers}}`

- Mostra i logs di un container in un pod o in una risorsa specificata:

`kubectl logs {{nome_pod}}`

- Esegue un commando in un pod esistente:

`kubectl exec {{nome_pod}} -- {{ls /}}`
