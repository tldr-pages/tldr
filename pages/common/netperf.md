# netperf

> Client-side command for `netperf`, the benchmarking application that measures network throughput. Similar to `iperf`.
> See also: `netserver` for the server-side command.
> Homepage: <https://hewlettpackard.github.io/netperf/>.

- Connect to server on a specific IP address via default port (12865):

`netperf {{address}}`

- Specify port:

`netperf {{address}} -p {{port}}`

- Specify number of seconds to run sampling (default is 10 seconds):

`netperf {{address}} -l {{seconds}}`

- Force IPv4 (or IPv6):

`netperf {{address}} -4`
