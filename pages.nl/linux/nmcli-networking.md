# nmcli networking

> Beheer de netwerkstatus van NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Toon de netwerkstatus van NetworkManager:

`nmcli {{[n|networking]}}`

- Schakel netwerk in/uit en alle interfaces die worden beheerd door NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- Toon de laatst bekende connectiviteitsstatus:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- Toon de huidige connectiviteitsstatus:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
