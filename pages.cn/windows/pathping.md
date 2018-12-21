# pathping

> A trace route tool combining features of `ping` and `tracert`.

- Ping and trace the route to a host:

`pathping {{hostname}}`

- Do not perform reverse lookup of ip-address to hostname:

`pathping {{hostname}} -n`

- Specify the maximum number of hops to search for the target (the default is 30):

`pathping {{hostname}} -h {{max_hops}}`

- Specify the milliseconds to wait between pings (the default is 240):

`pathping {{hostname}} -p {{time}}`

- Specify the number of queries per hop (the default is 100):

`pathping {{hostname}} -q {{queries}}`

- Force IPV4 usage:

`pathping {{hostname}} -4`

- Force IPV6 usage:

`pathping {{hostname}} -6`

- Display detailed usage information:

`pathping /?`
