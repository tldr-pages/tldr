# sslstrip

> Realiza ataques de stripping de Secure Sockets Layer (SSL) basados en el trabajo de Moxie Marlinspike.
> Realiza un ataque de suplantación de ARP en conjunto.
> Más información: <https://www.kali.org/tools/sslstrip/>.

- Registra sólo el tráfico HTTPS POST en el puerto 10000 por defecto:

`sslstrip`

- Registra sólo el tráfico HTTPS POST en el puerto 8080:

`sslstrip --listen={{8080}}`

- Registra todo el tráfico SSL hacia y desde el servidor en el puerto 8080:

`sslstrip --ssl --listen={{8080}}`

- Registra todo el tráfico SSL y HTTP hacia y desde el servidor en el puerto 8080:

`sslstrip --listen={{8080}} --all`

- Especifica la ruta del archivo para almacenar los registros:

`sslstrip --listen={{8080}} --write={{ruta/a/archivo}}`

- Muestra la ayuda:

`sslstrip --help`
