# iperf3

> Traffic generator for testing network bandwidth.
> More information: <https://iperf.fr/iperf-doc.php>.

- Run iperf3 as a server:

`iperf3 {{[-s|--server]}}`

- Run an iperf3 server on a specific port:

`iperf3 {{[-s|--server]}} {{[-p|--port]}} {{port}}`

- Start bandwidth test:

`iperf3 {{[-c|--client]}} {{server_ip}}`

- Run iperf3 in multiple parallel streams:

`iperf3 {{[-c|--client]}} {{server_ip}} {{[-P|--parallel]}} {{streams}}`

- Run the test in reverse direction (server sends data to client):

`iperf3 {{[-c|--client]}} {{server_ip}} {{[-R|--reverse]}}`

- Set the duration of the test:

`iperf3 {{[-c|--client]}} {{server_ip}} {{[-t|--time]}} {{seconds}}`
