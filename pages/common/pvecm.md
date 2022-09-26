# pvecm

> Proxmox VE Cluster Manager.
> More information: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Add the current node to an existing cluster:

`pvecm add {{hostname_or_ip}}`

- Add a node to the cluster configuration (internal use):

`pvecm addnode {{node}}`

- Return the version of the cluster join API available on this node:

`pvecm apiver`

- Generate new cluster configuration:

`pvecm create {{clustername}}`

- Remove a node from the cluster configuration:

`pvecm delnode {{node}}`

- Display the local view of the cluster nodes:

`pvecm nodes`

- Display the local view of the cluster status:

`pvecm status`
