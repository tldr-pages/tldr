# kubectl run

> Run pods in Kubernetes. Specifies pod generator to avoid deprecation error in some K8S versions.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Run an nginx pod and expose port 80:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --port 80`

- Run an nginx pod, setting the TEST_VAR environment variable:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --env="TEST_VAR=testing"`

- Show API calls that would be made to create an nginx container:

`kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run`

- Run an Ubuntu pod interactively, never restart it, and remove it when it exits:

`kubectl run --generator=run-pod/v1 -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Run an Ubuntu pod, overriding the default command with echo, and specifying custom arguments:

`kubectl run --generator=run-pod/v1 temp-ubuntu --image=ubuntu:20.04 --command -- echo arg1 arg2 arg3`
