# pvecm

> Proxmox VE Cluster Manager.
> More information: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Add the current node to an existing cluster:

`pvecm add {{hostname_or_ip}}`

- Add a node to the cluster configuration (internal use):

`pvecm {{[addn|addnode]}} {{node}}`

- Display the version of the cluster join API available on this node:

`pvecm {{[ap|apiver]}}`

- Generate new cluster configuration:

`pvecm {{[c|create]}} {{clustername}}`

- Remove a node from the cluster configuration:

`pvecm {{[d|delnode]}} {{node}}`

- Display the local view of the cluster nodes:

`pvecm {{[n|nodes]}}`

- Display the local view of the cluster status:

`pvecm {{[s|status]}}`
