# sshuttle

> Transparent proxy server that tunnels traffic over an SSH connection.
> Doesn't require admin, or any special setup on the remote SSH server.
> More information: <https://github.com/sshuttle/sshuttle>.

- Forward all IPv4 TCP traffic via a remote SSH server:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Forward all IPv4 TCP and DNS traffic:

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Use the tproxy method to forward all IPv4 and IPv6 traffic:

`sudo sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`
