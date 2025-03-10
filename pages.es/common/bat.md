# bat

> Imprime y concatena archivos.
> Un clon de `cat` con resaltado de sintaxis e integración con Git.
> Más información: <https://github.com/sharkdp/bat>.

- Imprime bellamente (pretty print) el contenido de uno o más archivos en `stdout`:

`bat {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Concatena varios archivos en el archivo destino:

`bat {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo_destino}}`

- Elimina decoraciones y desactiva la paginación (`--style plain` puede sustituirse por `-p`, o ambas opciones por `-pp`):

`bat --style plain --pager never {{ruta/al/archivo}}`

- Resalta una línea específica o un rango de líneas con un color de fondo diferente:

`bat {{[-H|--highlight-line]}} {{10|5:10|:10|10:|10:+5}} {{ruta/al/archivo}}`

- Muestra caracteres no imprimibles como espacio, tabulador o nueva línea:

`bat {{[-A|--show-all]}} {{ruta/al/archivo}}`

- Elimina todos los adornos excepto los números de línea en la salida:

`bat {{[-n|--number]}} {{ruta/al/archivo}}`

- Resalta sintácticamente un archivo JSON estableciendo explícitamente el lenguaje:

`bat {{[-l|--language]}} json {{ruta/al/archivo.json}}`

- Muestra todos los lenguajes soportados:

`bat {{[-L|--list-languages]}}`
