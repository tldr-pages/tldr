# ip link

> Gestiona interfaces de red.
> Más información: <https://manned.org/ip-link>.

- Muestra información sobre todas las interfaces de red:

`ip link`

- Muestra información sobre una interfaz de red específica:

`ip link show {{ethN}}`

- Establece una interfaz de red arriba (up) o abajo (down). Usa inglés:

`ip link set {{ethN}} {{up|down}}`

- Establece un nombre significativo a una interfaz de red:

`ip link set {{ethN}} alias "{{LAN Interface}}"`

- Cambia la dirección MAC de una interfaz de red:

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- Cambia el tamaño de MTU para una interfaz de red para usar marcos jumbo:

`ip link set {{ethN}} mtu {{9000}}`
