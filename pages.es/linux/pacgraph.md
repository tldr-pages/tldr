# pacgraph

> Dibuja un gráfico de los paquetes instalados a PNG/SVG/GUI/consola.
> Más información: <https://github.com/keenerd/pacgraph>.

- Crea un gráfico SVG y PNG:

`pacgraph`

- Crear un gráfico SVG:

`pacgraph --svg`

- Imprime resumen en la consola:

`pacgraph --console`

- Anula el nombre de archivo/ubicación por defecto (Nota: No especifiques la extensión del archivo):

`pacgraph --file={{ruta/al/archivo}}`

- Cambia el color de los paquetes que no son dependencias:

`pacgraph --top={{color}}`

- Cambia el color de los paquetes dependientes:

`pacgraph --dep={{color}}`

- Cambia el color de fondo de un gráfico:

`pacgraph --background={{color}}`

- Cambia el color de los enlaces entre paquetes:

`pacgraph --link={{color}}`
