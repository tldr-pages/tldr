# curl

> Transfiere datos desde o hacia un servidor.
> Admite la mayoría de los protocolos, incluyendo HTTP, HTTPS, FTP, SCP, etc.
> Ver también: `wcurl`, `wget`.
> Más información: <https://curl.se/docs/manpage.html>.

- Realiza una petición HTTP GET y vuelca el contenido en `stdout`:

`curl {{https://example.com}}`

- Realiza una petición HTTP GET, sigue cualquier redirección `3xx` y vuelca las cabeceras y el contenido en `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Descarga un archivo guardando la salida con el nombre indicado en la URL:

`curl {{[-O|--remote-name]}} {{https://example.com/archivo.zip}}`

- Envía datos codificados como formulario (petición POST de tipo `application/x-www-form-urlencoded`). Usa `--data @nombre_archivo` o `--data @'-'` para leer desde `stdin`:

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{nombre=bob}}' {{http://example.com/formulario}}`

- Envía una petición con una cabecera extra, usando un método HTTP personalizado y a través de un proxy (como BurpSuite), ignorando certificados autofirmados no seguros:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Envía datos en formato JSON especificando la cabecera Content-Type apropiada:

`curl {{[-d|--data]}} '{{{"nombre":"bob"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/usuarios/1234}}`

- Pasa un certificado de cliente y clave privada para la petición, omitiendo la validación del certificado:

`curl {{[-E|--cert]}} {{cliente.pem}} --key {{clave.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Resuelve un nombre de host a una dirección IP personalizada con salida detallada (similar a editar `/etc/hosts` para resolución DNS personalizada):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
