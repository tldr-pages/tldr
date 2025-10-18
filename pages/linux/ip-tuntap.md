# ip tuntap

> Manage TUN/TAP virtual network interfaces.
> More information: <https://manned.org/ip-tuntap>.

- Show all existing TUN/TAP devices:

`ip {{tuntap}}`

- Create a TUN device with a specific name:

`ip {{tuntap}} add dev {{tun0}} mode tun`

- Create a TAP device with a specific name:

`ip {{tuntap}} add dev {{tap0}} mode tap`

- Delete a TUN or TAP device:

`ip {{tuntap}} del dev {{tun0|tap0}} mode {{tun|tap}}`

- Set the owner (UID) of a TUN/TAP device:

`ip {{tuntap}} add dev {{tun0}} mode {{tun|tap}} user {{username}}`

- Set both owner (UID) and group (GID) for a TUN/TAP device:

`ip {{tuntap}} add dev {{tap0}} mode {{tap}} user {{username}} group {{groupname}}`

- Show detailed information about a specific TUN/TAP device:

`ip {{tuntap}} show dev {{tun0|tap0}}`
