# avahi-browse

> Muestra los servicios y hosts expuestos en la red local a través de mDNS/DNS-SD.
> Avahi es compatible con Bonjour (Zeroconf) encontrado en dispositivos Apple.
> Más información: <https://www.avahi.org/>.

- Lista los servicios disponibles en la red local junto con sus direcciones y puertos, ignorando los de la máquina local:

`avahi-browse --all --resolve --ignore-local`

- Lista rápidamente los servicios en la red local en formato SSV para scripts:

`avahi-browse --all --terminate --parsable`

- Lista los dominios en el vecindario:

`avahi-browse --browse-domains`

- Limita la búsqueda a un dominio específico:

`avahi-browse --all --domain={{dominio}}`
