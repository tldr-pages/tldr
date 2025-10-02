# psping

> Una herramienta de ping que incluye ping TCP, medición de latencia y ancho de banda.
> Más información: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- Hace ping a un host usando ICMP:

`psping {{nombre_del_host}}`

- Hace ping a un host a través de un puerto TCP:

`psping {{nombre_del_host}}:{{puerto}}`

- Especifica el número de pings y lo lleva a cabo en silencio:

`psping {{nombre_del_host}} -n {{pings}} -q`

- Hace ping al objetivo a través de TCP 50 veces y produce un histograma de los resultados:

`psping {{nombre_del_host}}:{{puerto}} -q -n {{50}} -h`

- Muestra la ayuda:

`psping /?`
