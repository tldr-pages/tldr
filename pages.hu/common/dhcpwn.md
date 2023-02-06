# dhcpwn

> A DHCP IP-kimerítési támadások tesztelése és a helyi DHCP-forgalom kiszimatolása. További információ: <https://github.com/mschwager/dhcpwn>.

- Árassza el a hálózatot IP-kérelmekkel:

`dhcpwn --interface {{network_interface}} flood --count {{number_of_requests}}`

- A helyi DHCP-forgalom kiszimatolása:

`dhcpwn --interface {{network_interface}} sniff`
