# mitmdump

> Visualiza, registra y transforma mediante programación el tráfico HTTP.
> La versión de línea de comandos de mitmproxy.
> Más información: <https://docs.mitmproxy.org/stable/#mitmdump>.

- Inicia un proxy y guarda toda la salida en un archivo:

`mitmdump {{[-w|--wfile]}} {{ruta/al/archivo}}`

- Filtra un archivo de tráfico guardado para que solo contenga solicitudes POST:

`mitmdump {{[-nr|--no-server --read-flows]}} {{nombre_del_archivo_de_entrada}} {{[-w|--wfile]}} {{nombre_del_archivo_de_salida}} "{{~m post}}"`

- Reproduce un archivo de tráfico guardado:

`mitmdump {{[-nc|--no-server --client-replay]}} {{ruta/al/archivo}}`

- Intercepta tráfico DNS (inicia un servidor DNS de interceptación en 127.0.0.1:53):

`sudo mitmdump {{[-m|--mode]}} dns`
