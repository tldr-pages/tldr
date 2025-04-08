# ipcalc

> A tool to calculate IP information (subnet, broadcast, host range) from an IP address and netmask.
> More information: <https://github.com/ipcalc/ipcalc>.

- Display network info for an IP address:
`ipcalc {{192.168.0.1}}`

- Display network info using CIDR notation:
`ipcalc {{192.168.0.1/24}}`

- Display network info using a separate netmask:
`ipcalc {{192.168.0.1}} {{255.255.255.0}}`

- Show only CIDR notation output:
`ipcalc -c {{192.168.0.1/24}}`

- Show version information:
`ipcalc --version`
