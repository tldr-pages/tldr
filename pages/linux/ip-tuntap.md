# ip tuntap

> Manage TUN/TAP virtual network interfaces.
> More information: <https://baturin.org/docs/iproute2/#ip-tuntap>.

- Show all existing TUN/TAP devices:

`ip {{[tunt|tuntap]}}`

- Create a TUN device with a specific name:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0}} {{[m|mode]}} {{[t|tun]}}`

- Create a TAP device with a specific name:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tap0}} {{[m|mode]}} {{[t|tap]}}`

- Delete a TUN or TAP device:

`sudo ip {{[tunt|tuntap]}} {{[d|delete]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}}`

- Set the owner (UID) of a TUN/TAP device:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0}} {{[m|mode]}} {{tun|tap}} user {{username}}`

- Set both owner (UID) and group (GID) for a TUN/TAP device:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tap0}} {{[m|mode]}} {{tap}} user {{username}} group {{groupname}}`
