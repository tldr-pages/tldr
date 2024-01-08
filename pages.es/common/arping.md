# arping

> Descubre y sondea hosts en una red utilizando el protocolo ARP.
> Útil para el descubrimiento de direcciones MAC.
> Más información: <https://github.com/ThomasHabets/arping>.

- Haz ping a un host mediante paquetes de petición ARP:

`arping {{host_ip}}`

- Haz ping a un host en una interfaz específica:

`arping -I {{interfaz}} {{host_ip}}`

- Haz ping a un host y detenerse en la primera respuesta:

`arping -f {{host_ip}}`

- Haz ping a un host un determinado número de veces:

`arping -c {{cuenta}} {{host_ip}}`

- Emite paquetes de solicitud ARP para actualizar las cachés ARP de los vecinos:

`arping -U {{ip_a_retransmitir}}`

- Detecta direcciones IP duplicadas en la red enviando peticiones ARP con un tiempo de espera de 3 segundos:

`arping -D -w {{3}} {{ip_a_verificar}}`
