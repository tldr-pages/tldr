# ausearch

> Consulta el registro de auditoría de Linux en busca de eventos.
> Parte del paquete `audit`.
> Vea también: `audit2why`, `audit2allow`, `aureport`.
> Más información: <https://manned.org/ausearch>.

- Busca todos los eventos de denegación AVC de SELinux:

`sudo ausearch {{[-m|--message]}} avc`

- Busca eventos relacionados con un ejecutable específico:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- Busca eventos de un usuario específico:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- Busca eventos en los últimos 10 minutos:

`sudo ausearch {{[-ts|--start]}} recent`

- Busca intentos de inicio de sesión fallidos:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- Busca eventos relacionados con un archivo específico:

`sudo ausearch {{[-f|--file]}} {{ruta/al/archivo}}`

- Muestra los resultados en formato sin procesar para su posterior procesamiento:

`sudo ausearch {{[-m|--message]}} avc --raw`
