# ip netconf

> Display and modify network configuration parameters per interface.
> More information: <https://manned.org/ip-netconf>.

- Show network configuration for all interfaces:

`ip {{netconf}} show all`

- Show network configuration for a specific interface:

`ip {{netconf}} show dev {{network_interface}}`

- Show configuration for interfaces in a specific network namespace:

`ip {{netconf}} show name {{namespace}}`

- Show only IPv4 network configuration:

`ip -4 {{netconf}} show all`

- Show only IPv6 network configuration:

`ip -6 {{netconf}} show all`
