# nmcli general

> Administra los ajustes generales de NetworkManager.
> Este subcomando también se puede invocar con `nmcli g`.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- Muestra el estado general de NetworkManager:

`nmcli general`

- Muestra el nombre del host del dispositivo actual:

`nmcli general hostname`

- Cambia el nombre del host del dispositivo actual:

`sudo nmcli general hostname {{nuevo_nombre}}`

- Muestra los permisos de NetworkManager:

`nmcli general permissions`

- Muestra el nivel actual de registro (logging) y los dominios:

`nmcli general logging`

- Establece el nivel de registro y/o dominios (mira `man NetworkManager.conf` para todos los dominios disponibles):

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{dominio_1,dominio_2,...}}`
