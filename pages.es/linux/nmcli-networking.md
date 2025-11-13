# nmcli networking

> Administra el estado de red de NetworkManager.
> Este subcomando también se puede invocar con `nmcli n`.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Muestra el estado de red de NetworkManager:

`nmcli networking`

- Activa o desactiva redes y todas las interfaces gestionadas por NetworkManager:

`nmcli networking {{on|off}}`

- Muestra el último estado de conectividad conocido:

`nmcli networking connectivity`

- Muestra el estado de conectividad actual:

`nmcli networking connectivity check`
