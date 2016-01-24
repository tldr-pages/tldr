# ss

> Utility to investigate sockets.

- Show all TCP/UDP/RAW/UNIX sockets:

`ss -a {{-t/-u/-w/-x}}`

- Filter TCP sockets by states, only/exclude:

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- Show all TCP sockets connected to the local HTTPS port:

`ss -t src :{{443}}`

- Show all TCP sockets along with processes connected to a remote ssh port:

`ss -pt dst :{{ssh}}`

- Show all UDP sockets connected on a local port within a range:

`ss -u 'sport >= :{{lowest_port}} and sport <= :{{highest_port}}'`

- Show all TCP IPv4 sockets locally connected on the subnet 192.168.0.0/16:

`ss -4t {{192.168/16}}`
