# netstat

> Mostrar conexiones TCP activas, puertos en los que la computadora está escuchando, estadísticas del adaptador de red, la tabla de enrutamiento IP, estadísticas de IPv4 y estadísticas de IPv6.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Mostrar conexiones TCP activas:

`netstat`

- Mostrar todas las conexiones TCP activas y los puertos TCP y UDP en los que la computadora está escuchando:

`netstat -a`

- Mostrar estadísticas del adaptador de red, como el número de bytes y paquetes enviados y recibidos:

`netstat -e`

- Mostrar conexiones TCP activas y expresar direcciones y números de puerto numéricamente:

`netstat -n`

- Mostrar conexiones TCP activas e incluir el ID del proceso (PID) para cada conexión:

`netstat -o`

- Mostrar el contenido de la tabla de enrutamiento IP:

`netstat -r`

- Mostrar estadísticas por protocolo:

`netstat -s`

- Mostrar una lista de puertos actualmente abiertos y direcciones IP relacionadas:

`netstat -an`
