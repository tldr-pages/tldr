# kubectl get

> Abfragen von Kubernetes Resourcen und Objekten.
> Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get>.

- Zeige alle Namespaces im Cluster an:

`kubectl get namespaces`

- Frage alle Nodes in einem bestimmten [n]amespace ab:

`kubectl get nodes {{[-n|--namespace]}} {{namespace}}`

- Frage alle Pods in einem bestimmten [n]amespace ab:

`kubectl get pods {{[-n|--namespace]}} {{namespace}}`

- Frage alle Deployments in einem bestimmten [n]amespace ab:

`kubectl get deployments {{[-n|--namespace]}} {{namespace}}`

- Frage alle Services in einem bestimmten [n]amespace ab:

`kubectl get services {{[-n|--namespace]}} {{namespace}}`

- Frage alle Resourcen in einem bestimmten [n]amespace ab:

`kubectl get all {{[-n|--namespace]}} {{namespace}}`

- Frage alle Ressourcen ab, die in einer YAML Datei definiert sind:

`kubectl get {{[-f|--filename]}} {{pfad/zu/manifest.yaml}}`
