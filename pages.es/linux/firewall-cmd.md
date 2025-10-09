# firewall-cmd

> El cliente de línea de comandos de firewalld.
> Visualiza y adapta el estado de configuración del firewall, sea en tiempo de ejecución o permanente.
> Más información: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- Visualiza todas las zonas y reglas del firewall disponibles en su estado de configuración en tiempo de ejecución:

`firewall-cmd --list-all-zones`

- Mueve permanentemente la interfaz a la zona de bloqueo, bloqueando efectivamente toda comunicación:

`firewall-cmd --permanent --zone {{block}} --change-interface {{enp1s0}}`

- Abre permanentemente el puerto para un servicio en la zona especificada (como el puerto 443 cuando está en la zona `public`):

`firewall-cmd --permanent --zone {{public}} --add-service {{https}}`

- Cierra permanentemente el puerto para un servicio en la zona especificada (como el puerto 80 cuando está en la zona `public`):

`firewall-cmd --permanent --zone {{public}} --remove-service {{http}}`

- Reenvía permanentemente un puerto para paquetes entrantes en la zona especificada (como el puerto 443 al 8443 cuando entra en la zona `public`):

`firewall-cmd --permanent --zone {{public}} --add-rich-rule 'rule family "{{ipv4|ipv6}}" forward-port port "{{443}}" protocol "{{udp|tcp}}" to-port "{{8443}}"'`

- Recarga firewall para perder cualquier cambio en tiempo de ejecución y forzar que la configuración permanente tome efecto inmediatamente:

`firewall-cmd --reload`

- Guarda el estado de configuración de tiempo de ejecución en la configuración permanente:

`firewall-cmd --runtime-to-permanent`

- Habilita el modo pánico en caso de emergencia. Todo el tráfico es descartado, cualquier conexión activa será terminada:

`firewall-cmd --panic-on`
