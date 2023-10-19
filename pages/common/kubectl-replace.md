# kubctl replace

> Replace a resource by file name or stdin.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- Replace a pod using the pod definition file:

`kubectl replace -f {{pod_defination_file}}`

- Replace a pod based on the input passed into stdin:

`cat pod.yaml | kubectl replace -f -`

- Force replace, delete and then re-create the resource:

`kubectl replace --force -f {{pod_defination_file}}`
