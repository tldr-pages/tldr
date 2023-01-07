# kubectl get

> Abfragen von Kubernetes Resourcen und Objekten.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Zeige alle Namespaces im Cluster an:

`kubectl get namespaces`

- Frage alle Nodes in einem bestimmten Namespace ab:

`kubectl get nodes --namespace {{namespace}}`

- Frage alle Pods in einem bestimmten Namespace ab:

`kubectl get pods --namespace {{namespace}}`

- Frage alle Deployments in einem bestimmten Namespace ab:

`kubectl get deployments --namespace {{namespace}}`

- Frage alle Services in einem bestimmten Namespace ab:

`kubectl get services --namespace {{namespace}}`

- Frage alle Resourcen in einem bestimmten Namespace ab:

`kubectl get all --namespace {{namespace}}`

- Frage alle Ressourcen ab, die in einer YAML Datei definiert sind:

`kubectl get -f {{pfad/zu/manifest.yaml}}`
