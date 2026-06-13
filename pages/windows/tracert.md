# tracert

> Receive information about each step in the route between your PC and the target.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- Trace a route:

`tracert {{ip}}`

- Prevent `tracert` from resolving IP addresses to hostnames:

`tracert /d {{ip}}`

- Force `tracert` to use IPv4 only:

`tracert /4 {{ip}}`

- Force `tracert` to use IPv6 only:

`tracert /6 {{ip}}`

- Specify the maximum number of hops in the search for the target:

`tracert /h {{max_hops}} {{ip}}`

- Display help:

`tracert /?`
