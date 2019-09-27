# lxc

> Manage Linux containers using the lxd REST API.
> Any container names or patterns can be prefixed with the name of a remote server.

- List local containers matching a string. Omit the string to list all local containers:

`lxc list {{match_string}}`

- List images matching a string. Omit the string to list all images:

`lxc image list [{{remote}}:]{{match_string}}`

- Create a new container from an image:

`lxc init [{{remote}}:]{{image}} {{container}}`

- Start a container:

`lxc start [{{remote}}:]{{container}}`

- Stop a container:

`lxc stop [{{remote}}:]{{container}}`

- Show detailed info about a container:

`lxc info [{{remote}}:]{{container}}`

- Take a snapshot of a container:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`
