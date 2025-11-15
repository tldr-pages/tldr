# nmcli networking

> Manage the networking status of NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Show the networking status of NetworkManager:

`nmcli {{[n|networking]}}`

- Enable or disable networking and all interfaces managed by NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- Show the last known connectivity state:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- Show the current connectivity state:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
