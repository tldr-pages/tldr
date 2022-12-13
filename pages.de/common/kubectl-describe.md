# kubectl describe

> Details von Kubernetes-Objekten und -Ressourcen anzeigen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Zeige Details zu Pods in einem bestimmten Namespace an:

`kubectl describe pods -n {{namespace}}`

- Zeige Details zu Nodes in einem bestimmten Namespace an:

`kubectl describe nodes -n {{namespace}}`

- Zeige Details zu einem bestimmten Pod in einem bestimmten Namespace an:

`kubectl describe pods {{pod_name}} -n {{namespace}}`

- Zeige Details zu einer bestimmten Node in einem bestimmten Namespace an:

`kubectl describe nodes {{node_name}} -n {{namespace}}`

- Zeige Details zu Ressourcen, die in einer YAML Datei definiert sind, an:

`kubectl describe -f {{pfad/zu/manifest.yaml}}`
