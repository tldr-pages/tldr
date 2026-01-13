# ip

> Gestisce le configurazioni IP.
> Accessibile in modalità configurazione.
> Maggiori informazioni: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- Imposta la versione SSH:

`ip ssh version {{2}}`

- Imposta l'indirizzo del dispositivo (eseguito sotto il comando `interface`):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- Imposta l'indirizzo da determinare con DHCP (eseguito sotto il comando `interface`):

`ip address dhcp`

- Definisce un nome di dominio:

`ip domain-name {{example.com}}`
