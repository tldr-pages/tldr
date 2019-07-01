# sshuttle

> Transparent proxy server that tunnels traffic over an SSH connection.
> Doesn't require root or any special setup on the remote SSH server, though root access on the local machine is prompted for.

- Forward all IPv4 TCP traffic via a remote SSH server:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Also forward all DNS traffic to the server's default DNS resolver:

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Forward all traffic except that which is bound for a specific subnet:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- Use the tproxy method to forward all IPv4 and IPv6 traffic:

`sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`
