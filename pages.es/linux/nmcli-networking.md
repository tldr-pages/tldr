# nmcli networking

> Administra el estado de red de NetworkManager.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Muestra el estado de red de NetworkManager:

`nmcli {{[n|networking]}}`

- Activa o desactiva redes y todas las interfaces gestionadas por NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- Muestra el último estado de conectividad conocido:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- Muestra el estado de conectividad actual:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
