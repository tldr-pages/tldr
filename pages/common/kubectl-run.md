# kubectl run

> Run pods in Kubernetes.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Start an nginx pod and expost port 80

kubectl run nginx --image=nginx --port 80 

- Run an nginx pod, setting the TEST_VAR environment variable:

`kubectl run nginx --image=nginx --env="TEST_VAR=testing"`

- Show API calls that would be made to create an nginx container:

`kubectl run nginx --image=nginx --dry-run=client`

- Run a one-off Ubuntu pod interactively, never restart it, and remove it when it exits:

`kubectl run -it temp-ubuntu --image=ubuntu:20.04 --restart=Never --rm -- /bin/bash`

- Run a Ubuntu pod overriding the default command with echo and specifying custom arguments:

`kubectl run nginx --image=nginx --command -- echo arg1 arg2 arg3`