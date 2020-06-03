# macchanger

> Command line utility for manipulating network interface MAC addresses

- View current and permanent MAC address of interface:

`macchanger -s {{interface}}`

- Set interface to random MAC:

`macchanger -r {{interface}}`

- Set interface to specific MAC:

`macchanger -m {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Reset interface to permanent hardware MAC:

`macchanger -p {{interface}}`
