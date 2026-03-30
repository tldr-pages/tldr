# xargs

> Ejecuta un comando con argumentos canalizados provenientes de otro comando, un archivo, etc.
> La entrada se trata como un único bloque de texto y se divide en partes separadas por espacios, tabulaciones, saltos de línea y fin de archivo.
> Vea también: `parallel`.
> Más información: <https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs>.

- Ejecuta un comando usando los datos de entrada como argumentos:

`{{fuente_de_argumentos}} | xargs {{comando}}`

- Ejecuta múltiples comandos encadenados sobre los datos de entrada:

`{{fuente_de_argumentos}} | xargs sh -c "{{comando1}} && {{comando2}} | {{comando3}}"`

- Ejecuta un nuevo comando con cada argumento:

`{{fuente_de_argumentos}} | xargs {{[-n|--max-args]}} 1 {{comando}}`

- Aumenta el límite de procesos paralelos a 10 (el predeterminado es 1; 0 significa tantos procesos como sea posible):

`{{fuente_de_argumentos}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{comando}}`

- Ejecuta el comando una vez por cada línea de entrada, reemplazando las ocurrencias del marcador (aquí indicado como `_`) con la línea de entrada:

`{{fuente_de_argumentos}} | xargs -I _ {{comando}} _ {{argumentos_opcionales_extra}}`

- Solicita confirmación al usuario antes de ejecutar el comando (confirma con `y` o `Y`):

`{{fuente_de_argumentos}} | xargs {{[-p|--interactive]}} {{comando}}`

- Lee un archivo para obtener los argumentos que se pasarán a un comando:

`xargs {{[-a|--arg-file]}} {{ruta/al/archivo}} {{comando}}`

- Permite que el comando acceda al terminal para entrada interactiva:

`{{fuente_de_argumentos}} | xargs {{[-o|--open-tty]}} {{comando}}`
