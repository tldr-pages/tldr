# bridge

> Show and manipulate network bridge addresses and devices.
> More information: <https://manned.org/bridge>.

- List all bridges and their interfaces:

`bridge {{[l|link]}}`

- Show port vlan information:

`bridge {{[v|vlan]}}`

- Assign a VLAN to a port:

`sudo bridge {{[v|vlan]}} {{[a|add]}} dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- Remove a VLAN from a port:

`sudo bridge {{[v|vlan]}} {{[d|delete]}} dev {{lanX}} vid {{vlan_id}}`

- Watch for changes in bridge interfaces:

`bridge {{[mo|monitor]}}`

- Display help:

`bridge {{[h|help]}}`
