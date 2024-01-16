# netserver

> Server-side command for `netperf`, the benchmarking application that measures network throughput.
> See also: `netperf` for the client-side command.
> Homepage: <https://hewlettpackard.github.io/netperf/>.

- Start a server on the default port (12865) and fork to background:

`netserver`

- Start server in foreground and do not fork:

`netserver -D`

- Specify port:

`netserver -p {{port}}`

- Force IPv4 (or IPv6):

`netserver -4`
