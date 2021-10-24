# kube-fzf

> Shell commands for command-line fuzzy searching of Kubernetes Pods.
> See also `kubectl` for related commands.
> More information: <https://github.com/thecasualcoder/kube-fzf>.

- Get pod details (from current namespace):

`findpod`

- Get pod details (from all namespaces):

`findpod -a`

- Describe a pod:

`describepod`

- Tail pod logs:

`tailpod`

- Exec into a pod's container:

`execpod {{shell_command}}`

- Port-forward a pod:

`pfpod {{port_number}}`
