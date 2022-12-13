# nc

> The `nc` (or `netcat`) utility is used for just about anything under the sun involving TCP, UDP, or UNIX-domain sockets. It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning.
> More information: <http://man.openbsd.org/OpenBSD-current/man1/nc.1>.

- Use IPv[4] addressing only:

`nc -4 "{{host}}" "{{port}}"`

- Use IPv[6] addressing only:

`nc -6 "{{host}}" "{{port}}"`

- [u]DP instead of TCP:

`nc -u "{{host}}" "{{port}}"`

- Use [r]andom port number:

`nc -r "{{host}}"`

- [l]isten for an incoming connection rather than initiate connection:

`nc -l "{{host}}" "{{port}}"`

- Continue [l]istening for connections after first client has disconnected:

`nc -k -l "{{host}}" "{{port}}"`

- [n]o DNS lookups on addresses, hostnames or ports:

`nc -n "{{host}}" "{{port}}"`
