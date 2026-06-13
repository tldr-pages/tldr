# nmcli device

> Gestiona interfaces de red y establece nuevas conexiones WiFi usando NetworkManager.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- Muestra los estados de todas las interfaces de red:

`nmcli {{[d|device]}}`

- Muestra los puntos de acceso WiFi disponibles:

`nmcli {{[d|device]}} {{[w|wifi]}}`

- Se conecta a una red WiFi con el SSID especificado (se te pedirá una contraseña):

`nmcli {{[d|device]}} {{[w|wifi]}} {{[c|connect]}} {{ssid}} {{[-a|--ask]}}`

- Muestra la contraseña y el código QR para la red WiFi actual:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[s|show-password]}}`

- Imprime información detallada sobre un dispositivo:

`nmcli {{[d|device]}} {{[sh|show]}} {{wlan0}}`
