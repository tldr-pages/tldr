# avahi-browse

> Muestra los servicios y hosts expuestos en la red local a través de mDNS/DNS-SD.
> Avahi es compatible con Bonjour (Zeroconf) encontrado en dispositivos Apple.
> Más información: <https://manned.org/avahi-browse>.

- Lista los servicios disponibles en la red local junto con sus direcciones y puertos, ignorando los de la máquina local:

`avahi-browse {{[-a|--all]}} {{[-r|--resolve]}} {{[-l|--ignore-local]}}`

- Lista rápidamente los servicios en la red local en formato SSV para scripts:

`avahi-browse {{[-a|--all]}} {{[-t|--terminate]}} {{[-p|--parsable]}}`

- Lista los dominios en el vecindario:

`avahi-browse {{[-D|--browse-domains]}}`

- Limita la búsqueda a un dominio específico:

`avahi-browse {{[-a|--all]}} --domain={{dominio}}`
