# kubctl replace

> Replace a resource by file name or stdin.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- Replace the resource using the resource definition file:

`kubectl replace -f {{resource_defination_file}}`

- Replace the resource based on the input passed into stdin:

`cat {{resource_defination_file}} | kubectl replace -f -`

- Force replace, delete and then re-create the resource:

`kubectl replace --force -f {{resource_defination_file}}`
