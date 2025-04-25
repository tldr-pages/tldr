# dhcpwn

> Test DHCP IP exhaustion attacks and sniff local DHCP traffic.
> More information: <https://github.com/mschwager/dhcpwn>.

- Flood the network with IP requests:

`dhcpwn {{[-i|--interface]}} {{network_interface}} flood {{[-c|--count]}} {{number_of_requests}}`

- Sniff local DHCP traffic:

`dhcpwn {{[-i|--interface]}} {{network_interface}} sniff`
