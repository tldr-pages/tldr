# dhcpwn

> Testa attacchi di esaurimento IP DHCP ed intercetta il traffico DHCP locale.

- Inonda la rete con richieste di IP:

`dhcpwn --interface {{interfaccia}} flood --count {{numero_di_richieste}}`

- Intercetta traffico DHCP locale:

`dhcpwn --interface {{interfaccia}} sniff`
