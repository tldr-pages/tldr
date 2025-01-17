# tcpreplay

> Replay network traffic stored in a `pcap` file.
> More information: <https://tcpreplay.appneta.com/>.

- List available network interfaces:

`tcpreplay --listnics`

- Replay traffic to interface:

`tcpreplay -i {{eth0}} {{traffic.pcap}}`

- Replay traffic to interface and `stdout`:

`tcpreplay -i {{eth0}} --verbose {{traffic.pcap}}`

- Replay traffic to interface as fast as possible:

`tcpreplay -i {{eth0}} --topspeed {{traffic.pcap}}`

- Replay traffic to interface at given Mbps:

`tcpreplay -i {{eth0}} -M {{10}} {{traffic.pcap}}`

- Replay traffic to interface several times:

`tcpreplay -i {{eth0}} --loop={{num_times}} {{traffic.pcap}}`
