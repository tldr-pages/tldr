# ping.py

> Comprueba si se puede acceder a un host IPv4 mediante ICMP.
> Envía solicitudes de eco ICMP y espera las respuestas de eco.
> Nota: Requiere privilegios de root para acceder a sockets sin procesar (por ejemplo, ejecútelo con `sudo`).
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Realiza un ping a un host desde una dirección IPv4 de origen especificada:

`ping.py {{ipv4_origen}} {{ipv4_destino}}`

- Envía un ping a 192.168.1.100 desde 192.168.1.10:

`ping.py 192.168.1.10 192.168.1.100`
