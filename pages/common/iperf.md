# iperf

> Measure network bandwidth between computers.

- Run on server:

`iperf -s`

- Run on client:

`iperf -c {{server_address}}`

- Run 5 parallel threads on client:

`iperf -c {{server_address}} -P 5`
