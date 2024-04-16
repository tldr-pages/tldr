# difft

> Compara archivos o directorios basándose en la sintaxis del lenguaje de programación.
> Vea también: `delta`, `diff`.
> Más información: <https://difftastic.wilfred.me.uk/introduction.html>.

- Compara dos archivos o directorios:

`difft {{ruta/al/archivo_o_directorio1}} {{ruta/al/archivo_o_directorio2}}`

- Informa únicamente diferencias entre los archivos:

`difft --check-only {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Especifica el modo de visualización (por defecto es `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Ignora comentarios al comparar:

`difft --ignore-comments {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Activa/desactiva el resaltado sintáctico del código fuente (por defecto está activado):

`difft --syntax-highlight {{on|off}} {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- No muestra nada si no hay diferencias entre los archivos:

`difft --skip-unchanged {{ruta/al/archivo_o_directorio1}} {{ruta/al/archivo_o_directorio2}}`

- Imprime todos los lenguajes de programación admitidos por la herramienta, junto con sus extensiones:

`difft --list-languages`
