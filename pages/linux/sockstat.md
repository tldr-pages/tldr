# sockstat

> List open Internet or UNIX domain sockets.
> See also: `netstat`.
> More information: <https://manned.org/sockstat>.

- Show information for IPv4 and IPv6 sockets for both listening and connected sockets:

`sockstat`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific p[R]otocol:

`sockstat -{{4|6}} -l -R {{tcp|udp|raw|unix}} -p {{port1,port2...}}`

- Also show [c]onnected sockets and [u]nix sockets:

`sockstat -cu`

- Only show sockets of the specified `process_id` or process:

`sockstat -P {{process_id|process_name}}`

- Only show sockets of the specified `user_id` or user:

`sockstat -U {{user_id|username}}`

- Only show sockets of the specified `group_id` or group:

`sockstat -G {{group_id|group_name}}`
