# iperf

> Measure network bandwidth between computers.
> More information: <https://iperf.fr>.

- Run on server:

`iperf {{[-s|--server]}}`

- Run on server using UDP mode and set server port to listen on 5001:

`iperf {{[-u|--udp]}} {{[-s|--server]}} {{[-p|--port]}} {{5001}}`

- Run on client:

`iperf {{[-c|--client]}} {{server_address}}`

- Run on client every 2 seconds:

`iperf {{[-c|--client]}} {{server_address}} {{[-i|--interval]}} {{2}}`

- Run on client with 5 parallel threads:

`iperf {{[-c|--client]}} {{server_address}} {{[-P|--parallel]}} {{5}}`

- Run on client using UDP mode:

`iperf {{[-u|--udp]}} {{[-c|--client]}} {{server_address}} {{[-p|--port]}} {{5001}}`
