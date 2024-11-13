# iptables

> Configura tablas, cadenas y reglas del firewall IPv4 del kernel Linux.
> Utiliza `ip6tables` para establecer reglas para el tráfico IPv6. Vea también: `iptables-save`, `iptables-restore`.
> Más información: <https://manned.org/iptables>.

- Muestra cadenas, reglas, contadores de paquetes/bytes y números de línea para la tabla de filtros (filter table):

`sudo iptables --verbose --numeric --list --line-numbers`

- Establece la [p]olítica de cadena de la regla :

`sudo iptables --policy {{cadena}} {{regla}}`

- [a]ñade una regla a la política de cadena para la IP:

`sudo iptables --append {{cadena}} --source {{ip}} --jump {{regla}}`

- [a]ñade una regla a la política de cadena para la IP teniendo en cuenta el [p]rotocolo y el puerto:

`sudo iptables --append {{cadena}} --source {{ip}} --protocol {{tcp|udp|icmp|...}} --dport {{puerto}} --jump {{regla}}`

- Agrega una regla NAT para traducir todo el tráfico desde la subred `192.168.0.0/24` a la IP pública del host:

`sudo iptables --table {{nat}} --append {{POSTROUTING}} --source {{192.168.0.0/24}} --jump {{MASQUERADE}}`

- Borra la regla de la cadena:

`sudo iptables --delete {{cadena}} {{número_de_línea_de_regla}}`
