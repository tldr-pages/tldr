# lstopo

> Muestra la topología de hardware del sistema.
> Más información: <https://manned.org/lstopo>.

- Muestra la topología resumida del sistema en una ventana gráfica (o imprime en consola si no se dispone de una sesión gráfica):

`lstopo`

- Muestra la topología completa del sistema sin resúmenes:

`lstopo --no-factorize`

- Muestra la topología resumida del sistema sólo con índices físicos (es decir, tal y como la ve el sistema operativo):

`lstopo --physical`

- Escribe la topología completa del sistema en un archivo con el formato especificado:

`lstopo --no-factorize --output-format {{console|ascii|tex|fig|svg|pdf|ps|png|xml}} {{ruta/al/archivo}}`

- Muestra datos en monocromo o escala de grises:

`lstopo --palette {{none|grey}}`
