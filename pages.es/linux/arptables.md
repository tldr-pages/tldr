# arptables

> Gestiona las reglas de filtrado ARP usando el backend `nftables`.
> Parte de la suite `xtables-nft` para filtrado de paquetes ARP.
> Más información: <https://manned.org/arptables>.

- Lista todas las reglas ARP en la tabla de filtrado:

`sudo arptables {{[-L|--list]}}`

- Añade una regla para descartar paquetes ARP de una dirección IP específica:

`sudo arptables {{[-A|--append]}} INPUT {{[-s|--source-ip]}} {{192.168.0.1}} {{[-j|--jump]}} DROP`

- Elimina una regla específica de la cadena INPUT por su número de regla:

`sudo arptables {{[-D|--delete]}} INPUT {{número_de_regla}}`

- Borra todas las reglas de la tabla de filtros:

`sudo arptables {{[-F|--flush]}}`

- Establece la política predeterminada de la cadena OUTPUT en ACCEPT:

`sudo arptables {{[-P|--policy]}} OUTPUT ACCEPT`

- Guarda las reglas ARP actuales en un archivo:

`sudo arptables-save > {{ruta/a/archivo}}`
