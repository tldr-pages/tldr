# dhcpwn

> Testați atacurile de epuizare DHCP IP și adulmecă traficul local DHCP.
> Mai multe informaţii: <https://github.com/mschwager/dhcpwn>

- Inundați rețeaua cu cereri IP:

`dhcpwn --interface {{network_interface}} flood --count {{number_of_requests}}`

- Adulmecă traficul local DHCP:

`dhcpwn --interface {{network_interface}} sniff`
