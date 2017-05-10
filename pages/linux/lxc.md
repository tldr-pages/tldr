# lxc

> Manage Linux containers using the lxd REST API.
> In all cases, 'remote:' is optional and refers to the alias for a remote server (i.e. 'ubuntu:').

- List local containers matching a filter string. Omit the filter to list all local containers:

`lxc list {{filter}}`

- List images matching a filter string. Omit the filter to list all images:

`lxc image list {{remote}}:{{filter}}`

- Create a new container from an image:

`lxc launch {{remote}}:{{image}} {{container_name}}`

- Start a container:

`lxc start {{remote}}:{{container_name}}`

- Stop a container:

`lxc stop {{remote}}:{{container_name}}`

- Show detailed info about a container:

`lxc info {{remote}}:{{container_name}}`

- Take a snapshot of a container:

`lxc snapshot {{remote}}:{{container_name}} {{snapshot_name}}`
