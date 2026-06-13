# ipconfig

> Muestra y gestiona la configuración de red de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Lista todos los adaptadores de red:

`ipconfig`

- Muestra una lista detallada de los adaptadores de red:

`ipconfig /all`

- Renueva las direcciones IP para un adaptador de red:

`ipconfig /renew {{adaptador}}`

- Libera las direcciones IP para un adaptador de red:

`ipconfig /release {{adaptador}}`

- Muestra la caché DNS local:

`ipconfig /displaydns`

- Elimina todos los datos de la caché DNS local:

`ipconfig /flushdns`
