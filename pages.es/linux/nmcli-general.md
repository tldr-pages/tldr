# nmcli general

> Administra los ajustes generales de NetworkManager.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- Muestra el estado general de NetworkManager:

`nmcli {{[g|general]}}`

- Muestra el nombre del host del dispositivo actual:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- Cambia el nombre del host del dispositivo actual:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{nuevo_nombre}}`

- Muestra los permisos de NetworkManager:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- Muestra el nivel actual de registro (logging) y los dominios:

`nmcli {{[g|general]}} {{[l|logging]}}`

- Establece el nivel de registro y/o dominios (mira `man NetworkManager.conf` para todos los dominios disponibles):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{dominio_1,dominio_2,...}}`
