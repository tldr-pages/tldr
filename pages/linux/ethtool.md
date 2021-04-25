# ethtool

> Display and modify Network Interface Controller (NIC) parameters.
> More information: <http://man7.org/linux/man-pages/man8/ethtool.8.html>.

- Display the current settings for an interface:

`ethtool {{eth0}}`

- Display the driver information for an interface:

`ethtool --driver {{eth0}}`

- Display the network usage statistics for an interface:

`ethtool --statistics {{eth0}}`

- Blink one or more LEDs on an interface for 10 seconds:

`ethtool --identify {{eth0}} {{10}}`

- Set the link speed, duplex mode, and parameter autonegotiation for a given interface:

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`
