# kubectl

> Befehlszeilenschnittstelle zur Ausführung von Befehlen gegen Kubernetes-Cluster.
> Einige Unterbefehle wie `kubectl run` haben ihre eigene Dokumentation zur Verwendung.
> Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/>.

- Liste Informationen über eine Ressource mit weiteren Details auf:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Aktualisiere die angegebenen Pods mit dem Label 'unhealthy' und dem Wert 'true':

`kubectl label pods {{name}} unhealthy=true`

- Liste alle Ressourcen aller Typen auf:

`kubectl get all`

- Zeige die Ressourcennutzung (CPU/Memory/Storage) von Knoten oder Pods:

`kubectl top {{pod|node}}`

- Zeige die Adresse der Master- und Clusterdienste:

`kubectl cluster-info`

- Zeige eine Erklärung zu einem bestimmten Feld an:

`kubectl explain {{pods.spec.containers}}`

- Zeige Logs für einen Container in einem Pod oder einer bestimmten Ressource:

`kubectl logs {{pod_name}}`

- Führe einen Befehl in einem bestehenden Pod aus:

`kubectl exec {{pod_name}} -- {{ls /}}`
