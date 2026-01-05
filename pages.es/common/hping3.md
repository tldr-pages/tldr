# hping3

> Utilidad avanzada de ping que admite protocolos como TCP, UDP e IP sin procesar.
> Se recomienda ejecutarla con privilegios elevados.
> Vea también: `masscan`, `naabu`, `nmap`, `rustscan`, `zmap`.
> Más información: <https://manned.org/hping3>.

- Envía un ping a un destino con 4 solicitudes de ping ICMP:

`hping3 {{[-1|--icmp]}} {{[-c|--count]}} 4 {{ip_o_nombre_del_host}}`

- Hace ping a una dirección IP a través de UDP en el puerto 80:

`hping3 {{[-2|--udp]}} {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_o_nombre_del_host}}`

- Escanea el puerto TCP 80, escaneando desde el puerto local específico 5090:

`hping3 {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} 80 {{[-s|--baseport]}} 5090 {{ip_o_nombre_del_host}}`

- Traceroute utilizando un escaneo TCP a un puerto de destino específico:

`hping3 {{[-T|--traceroute]}} {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} {{80}} {{ip_o_nombre_del_host}}`

- Escaneo de un conjunto de puertos TCP en una dirección IP específica:

`hping3 {{[-8|--scan]}} {{80,3000,9000}} {{[-S|--syn]}} {{ip_o_nombre_del_host}}`

- Realiza un escaneo TCP ACK para comprobar si un host determinado está activo:

`hping3 {{[-c|--count]}} {{2}} {{[-V|--verbose]}} {{[-p|--destport]}} {{80}} {{[-A|--ack]}} {{ip_o_nombre_del_host}}`

- Realiza una prueba de carga en el puerto 80:

`hping3 --flood {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_o_nombre_del_host}}`
