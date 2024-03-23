# netperf

> Client-side command for `netperf`, the benchmarking application that measures network throughput. Similar to `iperf`.
> See also: `netserver`, for the server-side command.
> More information: <https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>.

- Connect to server on a specific IP address via default port (12865):

`netperf {{address}}`

- Specify [p]ort:

`netperf {{address}} -p {{port}}`

- Specify the sampling [l]ength in seconds (default is 10):

`netperf {{address}} -l {{seconds}}`

- Force IPv[4] or IPv[6]:

`netperf {{address}} -{{4|6}}`
