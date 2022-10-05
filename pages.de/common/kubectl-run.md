# kubectl run

> Pods in Kubernetes ausführen. Gibt den Pod-Generator an, um einen deprecation Fehler in einigen Kubernetes Versionen zu vermeiden..
> Mehr Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Einen nginx-Pod starten und Port 80 freigeben:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --port 80`

- Starten Sie einen nginx-Pod und setzen Sie die Umgebungsvariable TEST_VAR:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --env="TEST_VAR=testing"`

- API-Aufrufe anzeigen, die zur Erstellung eines Nginx-Containers erfolgen würden:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run`

- Einen Ubuntu-Pod interaktiv ausführen, ihn nie neu starten und ihn entfernen, wenn er beendet wird:

`kubectl run --generator=run-pod/v1 -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Führen Sie einen Ubuntu-Pod aus, überschreiben Sie den Standardbefehl mit echo und geben Sie eigene Argumente an:

`kubectl run --generator=run-pod/v1 temp-ubuntu --image=ubuntu:20.04 --command -- echo arg1 arg2 arg3`
