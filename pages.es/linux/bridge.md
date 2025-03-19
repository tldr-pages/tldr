# bridge

> Muestra y manipula las direcciones y dispositivos de los puentes de red.
> Más información: <https://manned.org/bridge>.

- Lista todos los puentes y sus interfaces:

`bridge {{[l|link]}}`

- Muestra información de vlan de puerto:

`bridge {{[v|vlan]}}`

- Asigna una VLAN a un puerto:

`sudo bridge {{[v|vlan]}} {{[a|add]}} dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- Eliminar una VLAN de un puerto:

`sudo bridge {{[v|vlan]}} {{[d|delete]}} dev {{lanX}} vid {{vlan_id}}`

- Vigila los cambios en las interfaces de bridge:

`bridge {{[mo|monitor]}}`
