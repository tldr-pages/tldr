# hping3

> Utilidad de ping avanzada que soporta protocolos TCP, UDP y raw IP.
> Mejor correrla con privilegios elevados.
> Más información: <https://github.com/antirez/hping>.

- Ping a un destino con 4 solicitudes ping ICMP:

`hping3 --icmp --count {{4}} {{ip_o_nombre_de_servidor}}`

- Ping a una dirección IP sobre UDP en el puerto 80:

`hping3 --udp --destport {{80}} --syn {{ip_o_nombre_de_servidor}}`

- Escanea el puerto TCP 80, haciéndolo desde el puerto de origen local 5090:

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_o_nombre_de_servidor}}`

- Traceroute utilizando un escaneado TCP a un puerto de destino específico:

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_o_nombre_de_servidor}}`

- Escanea un conjunto de puertos TCP en una dirección IP específica:

`hping3 --scan {{80,3000,9000}} --syn {{ip_o_nombre_de_servidor}}`

- Realiza un escaneado TCP ACK para comprobar si un equipo dado está vivo:

`hping3 --count {{2}} --verbose --destport {{80}} --ack {{ip_o_nombre_de_servidor}}`

- Realiza una prueba de carga en el puerto 80:

`hping3 --flood --destport {{80}} --syn {{ip_o_nombre_de_servidor}}`
