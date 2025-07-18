# nmcli networking

> Manage the networking status of NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show the networking status of NetworkManager:

`nmcli {{[n|networking]}}`

- Enable or disable networking and all interfaces managed by NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- Show the last known connectivity state:

`nmcli {{[n|networking]}} connectivity`

- Show the current connectivity state:

`nmcli {{[n|networking]}} connectivity check`
