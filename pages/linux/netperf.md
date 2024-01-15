# netperf

> Client-side command for the network throughput benchmarking application netperf. Similar to iperf.
> Homepage: <https://hewlettpackard.github.io/netperf/>.

- Connect to server on a specific IP address via default port (12865):

`netperf IP`

- Specify port:

`netperf IP -p 12345`

- Specify number of seconds to run sampling (default is 10 seconds):

`netperf IP -l SECONDS`

- Force IPv4 (or IPv6):

`netperf IP -4`

- To start a server, use netserver. This will use the default port and fork to background:

`netserver`
