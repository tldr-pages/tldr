# kubectl

> Befehlszeilenschnittstelle zur Ausführung von Befehlen gegen Kubernetes-Cluster.
> Einige Unterbefehle wie `kubectl run` haben ihre eigene Dokumentation zur Verwendung.
> Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/>.

- Informationen über eine Ressource mit weiteren Details auflisten:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Aktualisierung des angegebenen Pods mit dem Label 'unhealthy' und dem Wert 'true':

`kubectl label pods {{name}} unhealthy=true`

- Alle Ressourcen mit verschiedenen Typen auflisten:

`kubectl get all`

- Anzeige der Ressourcennutzung (CPU/Memory/Storage) von Knoten oder Pods:

`kubectl top {{pod|node}}`

- Zeigt die Adresse der Master- und Clusterdienste:

`kubectl cluster-info`

- Eine Erklärung zu einem bestimmten Feld anzeigen:

`kubectl explain {{pods.spec.containers}}`

- Zeigt Logs für einen Container in einem Pod oder einer bestimmten Ressource:

`kubectl logs {{pod_name}}`

- Befehl in einem bestehenden Pod ausführen:

`kubectl exec {{pod_name}} -- {{ls /}}`
