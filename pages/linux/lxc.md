# lxc

> Manage Linux containers using the lxd REST API.
> 'remote:' refers to the alias for a remote server (i.e. 'ubuntu:') and when omitted will apply locally.

- List local containers matching a string. Omit string to list all local containers:

`lxc list {{match_string}}`

- List images matching a string. Omit string to list all images:

`lxc image list [{{remote}}:]{{match_string}}`

- Create a new container from an image:

`lxc launch [{{remote}}:]{{image}} {{container}}`

- Start a container:

`lxc start [{{remote}}:]{{container}}`

- Stop a container:

`lxc stop [{{remote}}:]{{container}}`

- Show detailed info about a container:

`lxc info [{{remote}}:]{{container}}`

- Take a snapshot of a container:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`
