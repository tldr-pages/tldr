# macchanger

> Command-line utility for manipulating network interface MAC addresses.
> More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger --show {{interface}}`

- Set interface to a random MAC:

`macchanger --random {{interface}}`

- Set interface to a specific MAC:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Reset interface to its permanent hardware MAC:

`macchanger --permanent {{interface}}`
