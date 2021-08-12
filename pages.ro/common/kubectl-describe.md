# kubectl describe

> Afișați detaliile obiectelor și resurselor Kubernetes.
> Mai multe informaţii: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>

- Arată detalii despre păstăi într-un spațiu de nume:

`kubectl describe pods -n {{namespace}}`

- Afișează detaliile nodurilor într-un spațiu de nume:

`kubectl describe nodes -n {{namespace}}`

- Afișați detaliile unui anumit pod într-un spațiu de nume:

`kubectl describe pods {{pod_name}} -n {{namespace}}`

- Afișați detaliile unui anumit nod într-un spațiu de nume:

`kubectl describe nodes {{node_name}} -n {{namespace}}`

- Arată detaliile obiectelor Kubernetes definite într-un manifest YAML:

`kubectl describe -f {{path/to/manifest}}.yaml`
