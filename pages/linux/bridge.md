# bridge

> Show and manipulate network bridge addresses and devices.
> More information: <https://manned.org/a2disconf.8>.

- List all bridges and their interfaces:

`bridge {{[l|link]}}`

- Show port vlan information:

`bridge {{[v|vlan]}}`

- Assign a VLAN to a port:

`bridge {{[v|vlan]}} add dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- Remove a VLAN from a port:

`bridge {{[v|vlan]}} del dev {{lanX}} vid {{vlan_id}}`

- Watch for changes in bridge interfaces:

`bridge {{[mo|monitor]}}`
