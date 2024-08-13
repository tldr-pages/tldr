# ifconfig

> Netwerkinterface-configurator.
> Meer informatie: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Bekijk netwerkinstellingen van een Ethernet-adapter:

`ifconfig eth0`

- Toon details van alle interfaces, inclusief uitgeschakelde interfaces:

`ifconfig -a`

- Schakel de eth0-interface uit:

`ifconfig eth0 down`

- Schakel de eth0-interface in:

`ifconfig eth0 up`

- Ken een IP-adres toe aan de eth0-interface:

`ifconfig eth0 {{ip_adres}}`
