# psping

> A ping tool that includes TCP ping, latency and bandwidth measurement.
> More information: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- Ping a host using ICMP:

`psping {{hostname}}`

- Ping a host over a TCP port:

`psping {{hostname}}:{{port}}`

- Specify the number of pings and perform it quietly:

`psping {{hostname}} -n {{pings}} -q`

- Ping the target over TCP 50 times and produce a histogram of the results:

`psping {{hostname}}:{{port}} -q -n {{50}} -h`

- Display help:

`psping /?`
