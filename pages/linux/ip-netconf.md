# ip netconf

> Display configuration parameters.
> More information: <https://manned.org/ip-netconf>.

- Show network configuration for all interfaces:

`ip {{[netc|netconf]}}`

- Show network configuration for a specific interface:

`ip {{[netc|netconf]}} {{[s|show]}} dev {{network_interface}}`

- Show only IPv4 network configuration:

`ip -4 {{[netc|netconf]}}`

- Show only IPv6 network configuration:

`ip -6 {{[netc|netconf]}}`
