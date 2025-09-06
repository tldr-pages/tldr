# nmtui

> Interfaz de usuario de texto para controlar NetworkManager.
> Utilice `<ArrowKeys>` para navegar, tecla `<Enter>` para seleccionar una opción.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Abre la interfaz de usuario:

`nmtui`

- Lista las conexiones disponibles, con la opción de activarlas o desactivarlas:

`nmtui connect`

- Se conecta a una red dada:

`nmtui connect {{nombre|uuid|dispositivo|SSID}}`

- Edita, añade, elimina una red determinada:

`nmtui edit {{nombre|identificador}}`

- Establece el nombre de la máquina (hostname) ante la red:

`nmtui hostname`
