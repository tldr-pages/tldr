# pacgraph

> Dibuja un gráfico de los paquetes instalados a PNG/SVG/GUI/consola.
> Más información: <https://manned.org/pacgraph>.

- Crea un gráfico SVG y PNG:

`pacgraph`

- Crear un gráfico SVG:

`pacgraph {{[-s|--svg]}}`

- Imprime resumen en la consola:

`pacgraph {{[-c|--console]}}`

- Anula el nombre de archivo/ubicación por defecto (Nota: No especifiques la extensión del archivo):

`pacgraph {{[-f|--file]}} {{ruta/al/archivo}}`

- Cambia el color de los paquetes que no son dependencias:

`pacgraph {{[-t|--top]}} {{color}}`

- Cambia el color de los paquetes dependientes:

`pacgraph {{[-d|--dep]}} {{color}}`

- Cambia el color de fondo de un gráfico:

`pacgraph {{[-b|--background]}} {{color}}`

- Cambia el color de los enlaces entre paquetes:

`pacgraph {{[-l|--link]}} {{color}}`
