# mitmproxy

> Un proxy HTTP interactivo man-in-the-middle.
> Vea también: `mitmweb` y `mitmdump`.
> Más información: <https://docs.mitmproxy.org/stable/>.

- Inicia `mitmproxy` con la configuración por defecto (escuchará en el puerto `8080`):

`mitmproxy`

- Inicia `mitmproxy` con una dirección y puerto personalizados:

`mitmproxy --listen-host {{dirección_ip}} {{--listen-port|-p}} {{puerto}}`

- Inicia `mitmproxy` utilizando un script para procesar el tráfico:

`mitmproxy {{--scripts|-s}} {{ruta/a/script.py}}`

- Exporta los registros con las claves maestras SSL/TLS a programas externos (wireshark, etc.):

`SSLKEYLOGFILE="{{ruta/a/archivo}}" mitmproxy`

- Especifica el modo de funcionamiento del servidor proxy (`regular` es el predeterminado):

`mitmproxy {{--mode|-m}} {{regular|transparent|socks5|...}}`

- Configura el diseño de la consola:

`mitmproxy --console-layout {{horizontal|single|vertical}}`
