# macchanger

> Command-line utility for manipulating network interface MAC addresses.
> More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger --show {{interface}}`

- Set interface to a random MAC:

`macchanger --random {{interface}}`

- Set interface to a random MAC, and pretend to be a [b]urned-[i]n-[a]ddress:

`macchanger --random --bia {{interface}}`

- Set interface to a random vendor MAC of same/any kind:

`macchanger -{{a|A}} {{interface}}`

- Set interface to a specific MAC:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Print identification (first 3 pairs of MAC) of all known vendors:

`macchanger --list`

- Reset interface to its permanent hardware MAC:

`macchanger --permanent {{interface}}`
