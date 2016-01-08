# ss

> Utility to investigate sockets.

- Dump all TCP/UDP/RAW/UNIX sockets:

`ss -a {{-t/-u/-w/-x}}`

- Show process(es) that using socket:

`ss -p`

- Filter TCP sockets by states, only/exclude:

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- Filter sockets by address and/or port:

`ss -t dst 1.2.3.4:80`
`ss -u src 127/8`
`ss -t 'dport >= :1024'`
`ss -x "src /tmp/.X11-unix/*"`
`ss -t state established '( dport = :ssh or sport = :ssh )'`

- Only list IPv4 or IPv6 sockets:

`ss {{-4/-6}}`
