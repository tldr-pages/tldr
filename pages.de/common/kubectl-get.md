# kubectl get

> Abfragen von Kubernetes Resourcen und Objekten.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Alle Namespaces im aktuellen Cluster anzeigen:

`kubectl get namespaces`

- Frage alle Nodes in einem bestimmten Namespace ab:

`kubectl get nodes -n {{namespace}}`

- Frage alle Pods in einem spezifischen Namespace ab:

`kubectl get pods -n {{namespace}}`

- Alle Deployments in einem spezifischen Namepsace abfragen:

`kubectl get deployments -n {{namespace}}`

- Frage alle Services in einem spezifischen Namespace ab:

`kubectl get services -n {{namespace}}`

- Frage alle Resourcen in einem spezifischen Namespace ab:

`kubectl get all -n {{namespace}}`

- Alle Objekte abfragen, welche in einer YAML Datei definiert sind:

`kubectl get -f {{pfad/zu/manifest.yaml}}`
