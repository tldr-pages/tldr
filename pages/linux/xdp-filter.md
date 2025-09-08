# xdp-filter

> Load and manage an eBPF XDP packet filter.
> Part of the xdp-tools collection.
> More information: <https://github.com/xdp-project/xdp-tools/tree/main/xdp-filter>.

- Load the filter on an interface in skb (generic) mode with a default policy to allow unmatched traffic (if the default policy is allow, the list becomes a deny list and vice versa):

`sudo xdp-filter load --policy allow --mode {{skb}} {{eth0}}`

- Unload the filter from an interface:

`sudo xdp-filter unload {{eth0}}`

- Deny traffic to a specific destination port 
`sudo xdp-filter port {{8080}}`

- Deny traffic from a specific source IP address:

`sudo xdp-filter ip --mode src {{192.168.1.100}}`

- Deny traffic from a specific source MAC address:

`sudo xdp-filter ether --mode src {{1A:2B:3C:4D:5E:6F}}`

- Poll the packets XDP filter is processing every 10000 milliseconds and show the statistics 

`sudo xdp-filter poll --interval 10000`
