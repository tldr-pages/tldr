# crictl

> Manage CRI-compatible container runtimes.
> More information: <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

- List all kubernetes pods (Ready and NotReady):

`crictl pods`

- List all containers (Running and Exited):

`crictl ps {{[-a|--all]}}`

- List all images:

`crictl images`

- Print information about specific containers:

`crictl inspect {{container_id1 container_id2 ...}}`

- Open a specific shell inside a running container:

`crictl exec {{[-it|--interactive --tty]}} {{container_id}} {{sh}}`

- Pull a specific image from a registry:

`crictl pull {{image:tag}}`

- Print and follow logs of a specific container:

`crictl logs {{[-f|--follow]}} {{container_id}}`

- Remove one or more images:

`crictl rmi {{image_id1 image_id2 ...}}`
