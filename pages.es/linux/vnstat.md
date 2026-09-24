# vnstat

> Monitor de tráfico de red de línea de comandos.
> Más información: <https://manned.org/vnstat>.

- Muestra un resumen de tráfico de todas las interfaces:

`vnstat`

- Muestra un resumen de tráfico de una interfaz de red específica:

`vnstat {{[-i|--iface]}} {{interfaz_de_red}}`

- Muestra estadísticas en vivo de una interfaz de red específica:

`vnstat {{[-l|--live]}} {{[-i|--iface]}} {{interfaz_de_red}}`

- Muestra estadísticas de tráfico por hora durante las últimas 24 horas mediante un gráfico de barras:

`vnstat {{[-hg|--hoursgraph]}}`

- Mide y muestra el tráfico promedio por 30 segundos:

`vnstat {{[-tr|--traffic]}} {{30}}`
