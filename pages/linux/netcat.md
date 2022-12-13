# nc

> The `nc` (or `netcat`) utility is used for just about anything under the sun involving TCP, UDP, or UNIX-domain sockets. It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning.
> More information: <http://man.openbsd.org/OpenBSD-current/man1/nc.1>.


- Use IPv4 addressing only:

`nc -4 {{host}} {{port}}`

- Use IPv6 addressing only:

`nc -6 {{host}} {{port}}`

- UDP instead of TCP:

`nc -u {{host}} {{port}}`

- Use random port number:

`nc -r {{host}}`

- Listen for an incoming connection rather than initiate connection:

`nc -l {{host}} {{port}}`

- Continue listening for connections after first client has disconnected:

`nc -k -l {{host}} {{port}}`

- No DNS lookups on addresses, hostnames or ports:

`nc -n {{host}} {{port}}`
