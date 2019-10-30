# ethtool

> Display and modify Network Interface Controller (NIC) parameters.
> More information: <http://man7.org/linux/man-pages/man8/ethtool.8.html>.

- Set the link speed, duplex, and speed autonegotiation:

`ethtool -s {{interface}} speed {{10/100/1000}} duplex {{half/full}} autoneg {{on/off}}`
