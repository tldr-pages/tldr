# dhcpcd

> DHCP client.
> More information: <https://roy.marples.name/projects/dhcpcd>.

- Release all address leases:

`sudo dhcpcd {{[-k|--release]}}`

- Request the DHCP server for new leases:

`sudo dhcpcd {{[-n|--rebind]}}`
