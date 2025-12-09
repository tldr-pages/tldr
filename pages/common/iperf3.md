# iperf3

> Traffic generator for testing network bandwidth.
> More information: <https://iperf.fr/iperf-doc.php>.

- Run iperf3 as a server:

`iperf3 {{[-s|--server]}}`

- Run an iperf3 server on a specific port:

`iperf3 {{[-s|--server]}} {{[-p|--port]}} {{port}}`

- Start bandwidth test:

`iperf3 {{[-c|--client]}} {{server}}`

- Run iperf3 in multiple parallel streams:

`iperf3 {{[-c|--client]}} {{server}} {{[-P|--parallel]}} {{streams}}`

- Reverse direction of the test. Server sends data to the client:

`iperf3 {{[-c|--client]}} {{server}} {{[-R|--reverse]}}`
