# csrutil

> Gestionar la configuración de la Protección de Integridad del Sistema.
> Más información: <https://ss64.com/osx/csrutil.html>.

- Mstra el estado de la Protección de Integridad del Sistema:

`csrutil status`

- Desactiva la Protección de Integridad del Sistema:

`csrutil disable`

- Activa la Protección de Integridad del Sistema:

`csrutil enable`

- Muestra la lista de fuentes NetBoot permitidas:

`csrutil netboot list`

- Añade una dirección IPv4 a la lista de fuentes NetBoot permitidas:

`csrutil netboot add {{ip}}`

- Restablece el estado de Protección de integridad del Sistema y borra la lista NetBoot:

`csrutil clear`
