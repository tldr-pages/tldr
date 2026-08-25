# dhcpcd

> DHCP client.
> More information: <https://roy.marples.name/projects/dhcpcd>.

- Release all address leases:

`sudo dhcpcd {{[-k|--release]}}`

- Request the DHCP server for new leases:

`sudo dhcpcd {{[-n|--rebind]}}`

- Print (dump) the last acquired lease for a given interface:

`sudo dhcpcd {{[-U|--dumplease]}} {{interface_name}}`

- Print the last acquired lease for all interfaces:

`sudo dhcpcd {{[-U|--dumplease]}}`
