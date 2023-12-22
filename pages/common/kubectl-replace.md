# kubectl replace

> Replace a resource by file or `stdin`.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- Replace the resource using the resource definition file:

`kubectl replace -f {{path/to/file.yml}}`

- Replace the resource using the input passed into `stdin`:

`kubectl replace -f -`

- Force replace, delete and then re-create the resource:

`kubectl replace --force -f {{path/to/file.yml}}`
