# ifconfig

> Configurador de interfaces de red.
> Más información: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Vea la configuración de red de una interfaz:

`ifconfig {{nombre_de_la_interfaz}}`

- Muestra los detalles de todas las interfaces, incluidas las desactivadas:

`ifconfig -a`

- Desactiva una interfaz:

`ifconfig {{nombre_de_la_interfaz}} down`

- Habilita una interfaz:

`ifconfig {{nombre_de_la_interfaz}} up`

- Asigna una dirección IP a una interfaz:

`ifconfig {{nombre_de_la_interfaz}} {{dirección_ip}}`
