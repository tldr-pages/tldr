# nxc nfs

> Pentest and exploit NFS servers. Currently supports anonymous mode only.
> More information: <https://www.netexec.wiki/nfs-protocol>.

- Detect the version of a remote NFS server:

`nxc nfs {{192.168.178.0/24}}`

- List the available NFS shares:

`nxc nfs {{192.168.178.2}} --shares`

- Enumerate the exposed shares recursively to the specified depth:

`nxc nfs {{192.168.178.2}} --enum-shares {{5}}`

- Download the specified remote file:

`nxc nfs {{192.168.178.2}} --get-file {{path/to/remote_file}} {{path/to/local_file}}`

- Upload the specified local file to the remote share:

`nxc nfs {{192.168.178.2}} --put-file {{path/to/local_file}} {{path/to/remote_file}}`
