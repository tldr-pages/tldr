# nmcli connection

> Connection management with NetworkManager.
> More information: <https://man.archlinux.org/man/nmcli.1>.

- List all NetworkManager connections (shows name, uuid, type and device):

`nmcli connection`

- Activate a connection by specifying an uuid:

`nmcli connection up uuid {{uuid}}`

- Deactivate a connection:

`nmcli connection down uuid {{uuid}}`

- Create an auto-configured dual stack connection:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Create a static IPv6-only connection:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Create a static IPv4-only connection:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`
