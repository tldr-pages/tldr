# kubectl describe

> Details von Kubernetes-Objekten und -Ressourcen anzeigen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Zeige Details zu Pods in einem bestimmten Namespace an:

`kubectl describe pods --namespace="{{namespace}}"`

- Zeige Details zu Nodes in einem bestimmten Namespace an:

`kubectl describe nodes --namespace="{{namespace}}"`

- Zeige Details zu einem bestimmten Pod in einem bestimmten Namespace an:

`kubectl describe pods {{pod_name}} --namespace="{{namespace}}"`

- Zeige Details zu einer bestimmten Node in einem bestimmten Namespace an:

`kubectl describe nodes {{node_name}} --namespace="{{namespace}}"`

- Zeige Details zu Ressourcen, die in einer YAML Datei definiert sind, an:

`kubectl describe --filename={{pfad/zu/manifest.yaml}}`
