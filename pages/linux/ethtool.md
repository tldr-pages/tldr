# ethtool

> Display and modify Network Interface Controller (NIC) parameters.
> More information: <http://man7.org/linux/man-pages/man8/ethtool.8.html>.

- Set the link speed, duplex mode, and parameter autonegotiation for a given interface:

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`
