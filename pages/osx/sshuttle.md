# sshuttle

> Transparent proxy server that tunnels traffic over an SSH connection.
> Doesn't require admin, or any special setup on the remote SSH server.

- Forward all IPv4 TCP traffic via a remote SSH server:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Forward all IPv4 TCP and DNS traffic via a remote SSH server:

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Forward all IPv4 and IPv6 traffic via a remote SSH server:

`sudo sshuttle --remote={{username}}@{{sshserver}} --method=tproxy {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`
