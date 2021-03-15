# zeek

> Passive network traffic analyser.
> Any output and log files will be saved to the current working directory.
> More information: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- Analyse live traffic from a specific interface:

`sudo zeek --iface {{interface}}`

- Analyse live traffic from a specific interface and load custom scripts:

`sudo zeek --iface {{interface}} {{script1}} {{script2}}`

- Analyse live traffic from a specific interface, without loading any scripts:

`sudo zeek --bare-mode --iface {{interface}}`

- Analyse live traffic from a specific interface, applying a `tcpdump` filter:

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- Analyse live traffic from a specific interface using a watchdog timer:

`sudo zeek --watchdog --iface {{interface}}`

- Analyse traffic from a `pcap` file:

`sudo zeek --readfile {{path/to/file.trace}}`
