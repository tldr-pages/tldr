# pct

> LXC container manager.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- List all containers:

`pct list`

- Create a container (DRAFT):

`pct create`

- Show the configuration of a container, specifying its ID:

`pct config {{100}}`

- Start a specific container:

`pct start {{100}}`

- Send a shutdown request, then wait until the container is stopped:

`pct shutdown {{100}} && pct wait {{100}}`

- Destroy a container and remove all related resources:

`pct destroy {{100}} --purge`
