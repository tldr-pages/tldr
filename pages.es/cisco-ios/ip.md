# ip

> Administra configuraciones IP.
> Se accede en modo de configuración.
> Más información: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- Establece la versión de SSH:

`ip ssh version {{2}}`

- Asigna la dirección IP del dispositivo (esto se hace dentro del comando `interface`):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- Configura la dirección para que se obtenga mediante DHCP (esto se hace dentro del comando `interface`):

`ip address dhcp`

- Define un nombre de dominio:

`ip domain-name {{example.com}}`
