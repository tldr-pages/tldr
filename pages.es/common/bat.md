# bat

> Imprime y concatena archivos.
> Un clon de `cat` con resaltado de sintaxis e integración con `git`.

- Imprimir los contenidos de un archivo a la salida estándar (`stdout`):

`bat {{archivo}}`

- Concatenar varios archivos creando un nuevo archivo:

`bat {{archivo1}} {{archivo2}} > {{archivo_objetivo}}`

- Añade múltiples archivos al final de un archivo objetivo:

`bat {{archivo1}} {{archivo2}} >> {{archivo_objetivo}}`

- Numera las lineas del archivo:

`bat -n {{file}}`

- Muestra un archivo JSON con resaltado de sintaxis:

`bat --language json {{file.json}}`

- Muestra todos los lenguajes permitidos:

`bat --list-languages`
