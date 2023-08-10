# kubectl run

> Run pods in Kubernetes. Specifies pod generator to avoid deprecation error in some K8S versions.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Run an nginx pod and expose port 80:

`kubectl run {{nginx-dev}} --image=nginx --port 80`

- Run an nginx pod, setting the TEST_VAR environment variable:

`kubectl run {{nginx-dev}} --image=nginx --env="{{TEST_VAR}}={{testing}}"`

- Show API calls that would be made to create an nginx container:

`kubectl run {{nginx-dev}} --image=nginx --dry-run={{none|server|client}}`

- Run an Ubuntu pod interactively, never restart it, and remove it when it exits:

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- Run an Ubuntu pod, overriding the default command with echo, and specifying custom arguments:

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --command -- echo {{argument1 argument2 ...}}`
