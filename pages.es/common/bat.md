# bat

> Imprime y concatena archivos.
> Un clon de `cat` con resaltado de sintaxis e integración con Git.
> Más información: <https://github.com/sharkdp/bat>.

- Imprime los contenidos de un archivo a la salida estándar:

`bat {{archivo}}`

- Concatena varios archivos creando un nuevo archivo:

`bat {{archivo1}} {{archivo2}} > {{archivo_final}}`

- Añade múltiples archivos al final de un archivo objetivo:

`bat {{archivo1}} {{archivo2}} >> {{archivo_final}}`

- Numera las líneas del archivo:

`bat --number {{archivo}}`

- Muestra un archivo JSON con resaltado de sintaxis:

`bat --language json {{archivo.json}}`

- Muestra todos los lenguajes permitidos:

`bat --list-languages`
