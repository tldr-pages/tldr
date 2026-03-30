# openssl s_client

> Crea conexiones de cliente TLS.
> Más información: <https://docs.openssl.org/master/man1/openssl-s_client/>.

- Muestra las fechas de inicio y vencimiento del certificado de un dominio:

`openssl s_client -connect {{host}}:{{puerto}} 2>/dev/null | openssl x509 -noout -dates`

- Muestra el certificado presentado por un servidor SSL/TLS:

`openssl < /dev/null s_client -connect {{host}}:{{puerto}}`

- Establece el Indicador de Nombre de Servidor (SNI) al conectar al servidor SSL/TLS:

`openssl s_client -connect {{host}}:{{puerto}} -servername {{nombre_host}}`

- Muestra la cadena de certificados completa de un servidor HTTPS:

`openssl < /dev/null s_client -connect {{host}}:443 -showcerts`
