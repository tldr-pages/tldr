# kubectl rollout

> Verwalten des Rollouts einer Kubernetes-Ressource (deployments, daemonsets, and statefulsets).
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- Starte einen rollenden Neustart einer Ressource:

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- Überwache den fortlaufenden Aktualisierungsstatus einer Ressource:

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- Setze eine Ressource auf die vorherige Version zurück:

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- Zeige den Rollout-Verlauf einer Ressource an:

`kubectl rollout history {{resource_type}}/{{resource_name}}`
