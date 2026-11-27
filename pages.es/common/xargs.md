# xargs

> Ejecuta un comando con argumentos canalizados procedentes de otro comando, un archivo, etc.
> La entrada se trata como un único bloque de texto y se divide en partes separadas por espacios, tabulaciones, saltos de línea y fin de archivo.
> Vea también: `parallel`.
> Más información: <https://www.gnu.org/software/findutils/manual/find.html#xargs-options>.

- Ejecuta un comando utilizando los datos de entrada como argumentos:

`{{fuente_argumentos}} | xargs {{comando}}`

- Ejecuta varios comandos encadenados sobre los datos de entrada:

`{{fuente_argumentos}} | xargs sh -c "{{comando1}} && {{comando2}} | {{comando3}}"`

- Ejecuta un nuevo comando con cada argumento:

`{{fuente_argumentos}} | xargs {{[-n|--max-args]}} 1 {{comando}}`

- Aumenta el límite de procesos paralelos a 10 (el valor por defecto es 1; 0 significa tantos procesos como sea posible):

`{{fuente_argumentos}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{comando}}`

- Ejecuta el comando una vez por cada línea de entrada, sustituyendo cualquier aparición del marcador de posición (aquí marcado como `_`) por la línea de entrada:

`{{fuente_argumentos}} | xargs -I _ {{comando}} _ {{opcional_extra_argumentos}}`

- Solicita confirmación al usuario antes de ejecutar el comando (confirmar con `y` o `Y`):

`{{fuente_argumentos}} | xargs {{[-p|--interactive]}} {{comando}}`

- Lee un archivo para obtener los argumentos que se van a pasar a un comando:

`xargs {{[-a|--arg-file]}} {{ruta/al/archivo}} {{comando}}`

- Permite que el comando acceda al terminal para la entrada interactiva:

`{{fuente_argumentos}} | xargs {{[-o|--open-tty]}} {{comando}}`
