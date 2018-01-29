# iperf3

> Traffic generator for testing network bandwidth

- Run iperf3 as a server:

`iperf3 -s`

- Run an iperf3 server on a specific port:

`iperf3 -s -p{{port}}`

- Start bandwidth test:

`iperf3 -c{{server}}`

- Run iperf3 in multiple threads:

`iperf3 -c{{server}} -P{{threads}}`

- Reverse direction of the test. Server sends data to the client:

`iperf3 -c{{server}} -R`
