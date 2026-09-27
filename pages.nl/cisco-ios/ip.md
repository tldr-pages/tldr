# ip

> Beheer IP-configuraties.
> Toegankelijk in de configuratiemodus.
> Meer informatie: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- Stel de SSH-versie in:

`ip ssh version {{2}}`

- Stel het adres van het apparaat in (dit wordt gedaan onder het `interface`-commando):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- Laat het adres bepalen via DHCP (dit wordt gedaan onder het `interface`-commando):

`ip address dhcp`

- Definieer een domeinnaam:

`ip domain-name {{example.com}}`
