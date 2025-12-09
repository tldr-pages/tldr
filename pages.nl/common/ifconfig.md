# ifconfig

> Netwerkinterface-configurator.
> Meer informatie: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Bekijk netwerkinstellingen van een interface:

`ifconfig {{interface_naam}}`

- Toon details van alle interfaces, inclusief uitgeschakelde interfaces:

`ifconfig -a`

- Schakel een interface uit:

`ifconfig {{interface_naam}} down`

- Schakel een interface in:

`ifconfig {{interface_naam}} up`

- Ken een IP-adres toe aan een interface:

`ifconfig {{interface_naam}} {{ip_adres}}`
