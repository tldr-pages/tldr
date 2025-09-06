# nmcli networking

> Beheer de netwerk status of NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Toon de netwerk status of NetworkManager:

`nmcli {{[n|networking]}}`

- Schakel netwerk in/uit en alle interfaces die worden beheerd door NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- Toon de laatst bekende connectiviteit status:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- Toon de huidige connectiviteit status:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
