# kubectl run

> Rulați păstăi în Kubernetes. Specifică generatorul pod pentru a evita eroarea de învechire în unele versiuni K8S.
> Mai multe informaţii: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>

- Rulați un pod nginx și expuneți portul 80:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --port 80`

- Rulați un pod nginx, setând variabila de mediu TEST_VAR:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --env="TEST_VAR=testing"`

- Arată apeluri API care ar fi făcute pentru a crea un container nginx:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run`

- Rulați un pod Ubuntu interactiv, nu-l reporniți niciodată, și scoateți-l atunci când iese:

`kubectl run --generator=run-pod/v1 -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Rulați un pod Ubuntu, suprascriind comanda implicită cu ecou și specificând argumente personalizate:

`kubectl run --generator=run-pod/v1 temp-ubuntu --image=ubuntu:20.04 --command -- echo arg1 arg2 arg3`
