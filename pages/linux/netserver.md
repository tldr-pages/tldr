# netserver

> Server command for the network throughput benchmarking application, netperf.
> Homepage: <https://hewlettpackard.github.io/netperf/>.

- Start a server on the default port (12865) and fork to background:

`netserver`

- Start server in foreground and do not fork:

`netserver -D`

- Specify port:

`netserver -p 12345`

- Force IPv4 (or IPv6):

`netserver -4`

- To connect to the server, use netperf. This will sample send and receive throughput for 12 seconds:

`netperf ADDRESS -p PORT -l 12`
