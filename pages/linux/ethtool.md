# ethtool

> Display and modify Network Interface Controller (NIC) parameters.
> More information: <https://manned.org/ethtool>.

- Display the current settings for an interface:

`ethtool {{eth0}}`

- Display the driver information for an interface:

`ethtool {{[-i|--driver]}} {{eth0}}`

- Display all supported features for an interface:

`ethtool {{[-k|--show-features]}} {{eth0}}`

- Display the network usage statistics for an interface:

`ethtool {{[-S|--statistics]}} {{eth0}}`

- Blink one or more LEDs on an interface for 10 seconds:

`ethtool {{[-p|--identify]}} {{eth0}} {{10}}`

- Set the link speed, duplex mode, and parameter auto-negotiation for a given interface:

`ethtool {{[-s|--change]}} {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`
