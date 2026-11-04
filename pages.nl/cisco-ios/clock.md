# clock

> Stel de systeemklok in.
> Meer informatie: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- Stel de huidige datum en tijd in:

`clock set {{23}}:{{59}}:{{59}} {{30}} {{april}} {{2000}}`

- Onderhandel automatisch met de andere kant van de verbinding, met active-clock als standaard:

`clock active prefer`

- Onderhandel automatisch met de andere kant van de verbinding, met passive-clock als standaard:

`clock passive prefer`

- Toon de huidige klokmodus die door de firmware is onderhandeld:

`clock show interfaces`
