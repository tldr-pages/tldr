# kubectl run

> Pods in Kubernetes ausführen. Gibt den Pod-Generator an, um einen deprecation Fehler in einigen Kubernetes Versionen zu vermeiden.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Starte einen nginx-Pod und gib Port 80 frei:

`kubectl run {{nginx-dev}} --image=nginx --port 80`

- Starte einen nginx-Pod und setze die Umgebungsvariable TEST_VAR:

`kubectl run {{nginx-dev}} --image=nginx --env="{{TEST_VAR}}={{testing}}"`

- Zeige API-Aufrufe an, die zur Erstellung eines Nginx-Containers erfolgen würden:

`kubectl run {{nginx-dev}} --image=nginx --dry-run={{none|server|client}}`

- Führe einen Ubuntu-Pod interaktiv aus, starte ihn nie neu und entferne ihn, wenn er beendet wird:

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- Führe einen Ubuntu-Pod aus, überschreibe den Standardbefehl mit echo und gib eigene Argumente an:

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --command -- echo {{argument1 argument2 ...}}`
