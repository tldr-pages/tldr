# psping

> Una herramienta de ping que incluye ping TCP, medición de latencia y ancho de banda.
> Más información: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- Hacer ping a un host usando ICMP:

`psping {{nombre_del_host}}`

- Hacer ping a un host a través de un puerto TCP:

`psping {{nombre_del_host}}:{{puerto}}`

- Especificar el número de pings y realizarlo en silencio:

`psping {{nombre_del_host}} -n {{pings}} -q`

- Hacer ping al objetivo a través de TCP 50 veces y producir un histograma de los resultados:

`psping {{nombre_del_host}}:{{puerto}} -q -n {{50}} -h`

- Mostrar ayuda:

`psping /?`
