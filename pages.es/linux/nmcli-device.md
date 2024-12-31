# nmcli device

> Gestiona interfaces de red y establece nuevas conexiones WiFi usando NetworkManager.
> Este subcomando también puede llamarse con `nmcli d`.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Muestra los estados de todas las interfaces de red:

`nmcli device status`

- Muestra los puntos de acceso WiFi disponibles:

`nmcli device wifi`

- Se conecta a una red WiFi con el SSID especificado (se te pedirá una contraseña):

`nmcli --ask device wifi connect {{ssid}}`

- Muestra la contraseña y el código QR para la red WiFi actual:

`nmcli device wifi show-password`
