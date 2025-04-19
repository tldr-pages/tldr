# tcpreplay

> Replay network traffic stored in a `pcap` file.
> More information: <https://tcpreplay.appneta.com/>.

- List available network interfaces:

`tcpreplay --listnics`

- Replay traffic to interface:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{traffic.pcap}}`

- Replay traffic to interface and `stdout`:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-v|--verbose]}} {{traffic.pcap}}`

- Replay traffic to interface as fast as possible:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-t|--topspeed]}} {{traffic.pcap}}`

- Replay traffic to interface at given Mbps:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-M|--mbps]}} {{10}} {{traffic.pcap}}`

- Replay traffic to interface several times:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-l|--loop]}} {{num_times}} {{traffic.pcap}}`
