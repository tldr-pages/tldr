# torify

> Enruta el tráfico de red a través de la red Tor.
> Más información: <https://manned.org/man/torify>.

- Enruta el tráfico a través de Tor:

`torify {{comando}}`

- Activa Tor en el intérprete de comandos:

`torify {{on|off}}`

- Crea un intérprete de órdenes habilitado para Tor:

`torify --shell`

- Comprueba si hay un intérprete de órdenes habilitado para Tor:

`torify show`

- Especifica el archivo de configuración de Tor:

`torify -c {{archivo_de_configuración}} {{comando}}`

- Usa un proxy Tor SOCKS específico:

`torify -P {{proxy}} {{comando}}`

- Redirige la salida a un archivo:

`torify {{comando}} > {{ruta/a/archivo_de_salida}}`
