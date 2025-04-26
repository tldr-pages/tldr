# ipcalc

> Calculate IP information (subnet, broadcast, host range) from an IP address and netmask.
> More information: <https://manned.org/ipcalc>.

- Display network info for an IP address:

`ipcalc {{192.168.0.1}}`

- Display network info using CIDR notation:

`ipcalc {{192.168.0.1}}/{{24}}`

- Display network info using a dotted decimal netmask:

`ipcalc {{192.168.0.1}} {{255.255.255.0}}`

- Suppress bitwise output:

`ipcalc {{[-b|--nobinary]}} {{192.168.0.1}}`

- Split a network into specified sized blocks:

`ipcalc {{[-s|--split]}} {{size1 size2 size3 ...}} {{192.168.0.1}}`

- Show version information:

`ipcalc {{[-v|--version]}}`
