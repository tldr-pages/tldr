# ss

> Utility to investigate sockets

- Dump all TCP/UDP/RAW/UNIX sockets

`ss -a {{-t/-u/-w/-x}}`

- Filter TCP sockets by states, only/exclude

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- Filter sockets by address and/or port

`ss {{dst/src/dport/sport}} {{==/!=/>/</...}} {{prefix:port/unix:STRING/:port/...}}`

- Only list IPv4 or IPv6 sockets

`ss {{-4/-6}}`
