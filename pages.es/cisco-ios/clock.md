# clock

> Configura el reloj del sistema.
> Más información: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- Entra en el modo de ejecución privilegiado:

`clock set {{23}}:{{59}}:{{59}} {{31}} {{april}} {{2000}}`

- Negocia automáticamente con el extremo remoto del enlace, estableciendo por defecto el reloj activo:

`clock active prefer`

- Negocia automáticamente con el extremo remoto del enlace, estableciendo por defecto el reloj pasivo:

`clock passive prefer`

- Muestra el modo de reloj actual negociado por el firmware:

`clock show interfaces`
