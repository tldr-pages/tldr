# iw

> Muestra y manipula dispositivos inalámbricos.
> Vea también: `iw dev`, `nmcli`, `iwctl`.
> Más información: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Busca redes inalámbricas disponibles:

`iw dev {{wlp}} scan`

- Se conecta a una red inalámbrica abierta:

`iw dev {{wlp}} connect {{SSID}}`

- Cierra la conexión actual:

`iw dev {{wlp}} disconnect`

- Muestra información sobre la conexión actual:

`iw dev {{wlp}} link`

- Muestra todas las interfaces de red inalámbricas físicas y lógicas:

`iw dev`

- Muestra todas las capacidades inalámbricas de todas las interfaces de hardware físicas:

`iw phy`

- Muestra la información actual del dominio regulador inalámbrico del kernel:

`iw reg get`

- Muestra la ayuda:

`iw help`
