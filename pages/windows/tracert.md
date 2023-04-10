# tracert

> Receive information about each step in the route between your PC and the target.
> More information: <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb491018(v=technet.10)?redirectedfrom=MSDN>.

- Trace a route:

`tracert {{IP}}`

- Prevents tracert from resolving IP addresses to hostnames:

`tracert -d {{IP}}`

- Forces tracert to use IPv4 only:

`tracert -4 {{IP}}`

- Forces tracert to use IPv6 only:

`tracert -6 {{IP}}`

- Show detailed help:

`tracert /?`

- Specifies the maximum number of hops in the search for the target:

`tracert -h {{max_hops}} {{IP}}
