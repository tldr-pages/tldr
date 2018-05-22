# nrm

> JavaScript and Node.js package registry manager.
> Nrm can help you easy and fast switch between different npm registries, now include: npm, cnpm, taobao, nj(nodejitsu), rednpm.

- List all the registries:

`nrm ls`

- Change registry to registry:

`nrm use {{registry}}`

- Show the response time for one or all registries:

`nrm test [{{registry}}]`

- Add one custom registry:

`nrm add {{registry}} {{url}} [{{home}}]`

- Delete one custom registry:

`nrm del {{registry}}`

- Open the homepage of registry with optional browser:

`nrm home {{registry}} [{{browser}}]`
