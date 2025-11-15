# kubectl replace

> Replace a resource by file or `stdin`.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_replace>.

- Replace the resource using the resource definition file:

`kubectl replace {{[-f|--filename]}} {{path/to/file.yml}}`

- Replace the resource using the input passed into `stdin`:

`kubectl replace {{[-f|--filename]}} -`

- Force replace, delete and then re-create the resource:

`kubectl replace {{[-f|--filename]}} {{path/to/file.yml}} --force`
