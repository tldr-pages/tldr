# kubectl get

> Abfragen von Kubernetes Resourcen und Objekten.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Alle Namespaces im aktuellen Cluster anzeigen:

`kubectl get namespaces`

- Alle Nodes in spezifischen Namepsace abfragen:

`kubectl get nodes -n {{namespace}}`

- Alle Pods in einem spezifischen Namepsace abfragen:

`kubectl get pods -n {{namespace}}`

- Alle Deployments in einem spezifischen Namepsace abfragen:

`kubectl get deployments -n {{namespace}}`

- Alle Services in einem spezifischen Namepsace abfragen:

`kubectl get services -n {{namespace}}`

- Alle Resourcen in einem spezifischen Namepsace abfragen:

`kubectl get all -n {{namespace}}`

- Alle Objekte abfragen, welche in einer YAML Datei definiert sind:

`kubectl get -f {{pfad/zu/manifest}}.yaml`
