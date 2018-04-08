# iperf

> Measure network bandwidth between computers.

- Run on server:

`iperf -s`

- Run on client:

`iperf -c {{server_address}}`

- (On client) run 5 parallel threads:

`iperf -c {{server_address}} -P 5`
