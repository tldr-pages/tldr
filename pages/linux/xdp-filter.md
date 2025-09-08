# xdp-filter

> Load and manage an eBPF XDP packet filter.
> Part of the xdp-tools collection.
> More information: <https://github.com/xdp-project/xdp-tools/tree/main/xdp-filter>.

- Load the filter on an interface in skb (generic) mode with default allow policy:

`sudo xdp-filter load --policy allow --mode {{xdp_mode}} {{network_interface}}`

- Unload the filter from an interface:

`sudo xdp-filter unload {{network_interface}}`

- Deny traffic to a specific destination port:

`sudo xdp-filter port {{destination_port}}`

- Deny traffic from a specific source IP address:

`sudo xdp-filter ip --mode src {{source_ip}}`

- Deny traffic from a specific source MAC address:

`sudo xdp-filter ether --mode src {{mac_address}}`

- Poll packets and show statistics every 10000 milliseconds:

`sudo xdp-filter poll --interval 10000`
