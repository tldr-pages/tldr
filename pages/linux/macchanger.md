# macchanger

> Command line utility for manipulating network interface MAC addresses

- View current and permanent MAC address of interface:

`macchanger --show {{interface}}`

- Set interface to random MAC:

`macchanger --random {{interface}}`

- Set interface to specific MAC:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Reset interface to permanent hardware MAC:

`macchanger --permanent {{interface}}`
