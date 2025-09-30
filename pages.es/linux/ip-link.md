# ip link

> Gestiona interfaces de red.
> Más información: <https://manned.org/ip-link>.

- Muestra información sobre todas las interfaces de red:

`ip {{[l|link]}}`

- Muestra información sobre una interfaz de red específica:

`ip {{[l|link]}} {{[sh|show]}} {{ethN}}`

- Establece una interfaz de red arriba (up) o abajo (down). Usa inglés:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{up|down}}`

- Establece un nombre significativo a una interfaz de red:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[al|alias]}} "{{LAN Interface}}"`

- Cambia la dirección MAC de una interfaz de red:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- Cambia el tamaño de MTU para una interfaz de red para usar marcos jumbo:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} mtu {{9000}}`
