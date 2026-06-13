# netstat

> Muestra conexiones TCP activas, puertos en los que la computadora está escuchando, estadísticas del adaptador de red, la tabla de enrutamiento IP, estadísticas de IPv4 y estadísticas de IPv6.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Muestra conexiones TCP activas:

`netstat`

- Muestra todas las conexiones TCP activas y los puertos TCP y UDP en los que la computadora está escuchando:

`netstat -a`

- Muestra estadísticas del adaptador de red, como el número de bytes y paquetes enviados y recibidos:

`netstat -e`

- Muestra conexiones TCP activas y expresa direcciones y números de puerto numéricamente:

`netstat -n`

- Muestra conexiones TCP activas e incluye el ID del proceso (PID) para cada conexión:

`netstat -o`

- Muestra el contenido de la tabla de enrutamiento IP:

`netstat -r`

- Muestra estadísticas por protocolo:

`netstat -s`

- Muestra una lista de puertos actualmente abiertos y direcciones IP relacionadas:

`netstat -an`
