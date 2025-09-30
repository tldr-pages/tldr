# proxify

> Un proxy versátil y portátil para capturar, manipular y reproducir tráfico HTTP/HTTPS sobre la marcha.
> Vea también: `mitmproxy`.
> Más información: <https://github.com/projectdiscovery/proxify>.

- Inicia un proxy HTTP (en la interfaz de red loopback `127.0.0.1` y puerto `8888`):

`proxify`

- Inicia un proxy HTTP en una interfaz de red y puerto personalizados (puede requerir `sudo` para un número de puerto inferior a `1024`):

`proxify -http-addr "{{dirección_ip}}:{{número_de_puerto}}"`

- Especifica el formato y el archivo de salida:

`proxify -output-format {{jsonl|yaml}} -output {{ruta/al/archivo}}`

- Muestra la ayuda:

`proxify -h`
