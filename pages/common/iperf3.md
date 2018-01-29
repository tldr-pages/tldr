# iperf3

> Iperf3 — traffic generator for testing network bandwidth

- Run iperf3 as a server

`iperf3 -s`

- Run iperf3 server on port 5209

`iperf3 -s -p5209`

- Start bandwidth testing

`iperf3 -c {{server}}`

- Start bandwidth testing in 5 threads

`iperf3 -c {{server}} -P5`

- Start bandwidth testing in reverse mode

`iperf3 -c {{server}} -R`
