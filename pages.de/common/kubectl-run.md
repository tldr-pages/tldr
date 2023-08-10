# kubectl run

> Pods in Kubernetes ausführen. Gibt den Pod-Generator an, um einen deprecation Fehler in einigen Kubernetes Versionen zu vermeiden.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Starte einen nginx-Pod und gib Port 80 frei:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --port 80`

- Starte einen nginx-Pod und setze die Umgebungsvariable TEST_VAR:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --env="TEST_VAR=testing"`

- Zeige API-Aufrufe an, die zur Erstellung eines Nginx-Containers erfolgen würden:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run`

- Führe einen Ubuntu-Pod interaktiv aus, starte ihn nie neu und entferne ihn, wenn er beendet wird:

`kubectl run --generator=run-pod/v1 -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Führe einen Ubuntu-Pod aus, überschreibe den Standardbefehl mit echo und gib eigene Argumente an:

`kubectl run --generator=run-pod/v1 temp-ubuntu --image=ubuntu:20.04 --command -- echo {{argument1 argument2 ...}}`
