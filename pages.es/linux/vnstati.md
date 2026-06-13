# vnstati

> Genera imágenes PNG compatibles con vnStat.
> Más información: <https://manned.org/vnstati>.

- Genera un resumen de los últimos dos meses, días, etc:

`vnstati --summary --iface {{interfaz_de_red}} --output {{ruta/a/salida.png}}`

- Genera los 10 días con mayor tráfico de todos los tiempos:

`vnstati --top 10 --iface {{interfaz_de_red}} --output {{ruta/a/salida.png}}`

- Genera estadísticas de tráfico mensual de los últimos 12 meses:

`vnstati --months --iface {{interfaz_de_red}} --output {{ruta/a/salida.png}}`

- Genera estadísticas de tráfico por hora de las últimas 24 horas:

`vnstati --hours --iface {{interfaz_de_red}} --output {{ruta/a/salida.png}}`
