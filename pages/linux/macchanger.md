# macchanger

> Command-line utility for manipulating network interface MAC addresses.
> More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger {{[-s|--show]}} {{interface}}`

- Set interface to a random MAC:

`macchanger {{[-r|--random]}} {{interface}}`

- Set an interface to a random MAC address, and pretend to be a [b]urned-[i]n-[a]ddress:

`macchanger {{[-r|--random]}} {{[-b|--bia]}} {{interface}}`

- Set an interface to a specific MAC address:

`macchanger {{[-m|--mac]}} {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Print the identifications (the first three bytes of a MAC address) of all known vendors:

`macchanger {{[-l|--list]}}`

- Reset an interface to its permanent hardware MAC address:

`macchanger {{[-p|--permanent]}} {{interface}}`
