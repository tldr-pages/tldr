# macchanger

> Command-line utility for manipulating network interface MAC addresses.
> More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger --show {{interface}}`

- Set interface to a random MAC:

`macchanger --random {{interface}}`

- Set an interface to a random MAC address, and pretend to be a [b]urned-[i]n-[a]ddress:

`macchanger --random --bia {{interface}}`

- Set an interface to a specific MAC address:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Print the identifications (the first three bytes of a MAC address) of all known vendors:

`macchanger --list`

- Reset an interface to its permanent hardware MAC address:

`macchanger --permanent {{interface}}`
