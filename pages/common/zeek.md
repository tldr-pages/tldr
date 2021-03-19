# zeek

> Passive network traffic analyser.
> Any output and log files will be saved to the current working directory.
> More information: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- Analyze live traffic from a network interface:

`sudo zeek --iface {{interface}}`

- Analyze live traffic from a network interface and load custom scripts:

`sudo zeek --iface {{interface}} {{script1}} {{script2}}`

- Analyze live traffic from a network interface, without loading any scripts:

`sudo zeek --bare-mode --iface {{interface}}`

- Analyze live traffic from a network interface, applying a `tcpdump` filter:

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- Analyze live traffic from a network interface using a watchdog timer:

`sudo zeek --watchdog --iface {{interface}}`

- Analyze traffic from a `pcap` file:

`zeek --readfile {{path/to/file.trace}}`
