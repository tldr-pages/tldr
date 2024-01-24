# rargs

> Ejecuta un comando por cada línea de entrada estándar.
> Como `xargs`, pero con soporte de coincidencia de patrones.
> Más información: <https://github.com/lotabout/rargs>.

- Ejecuta un comando por cada línea de entrada, como `xargs` (`{0}` indica dónde sustituir en el texto):

`{{comando}} | rargs {{comando}} {0}`

- Realiza una ejecución en seco, lo cual imprime los comandos que se ejecutarían en lugar de ejecutarlos:

`{{comando}} | rargs -e {{comando}} {0}`

- Elimina la extensión `.bak` de todos los archivos de una lista:

`{{comando}} | rargs -p '(.*).bak mv {0} {1}`

- Ejecuta comandos en paralelo:

`{{command}} | rargs -w {{max-procs}}`

- Considera cada línea de entrada separada por un carácter NUL (`\0`) en lugar de una nueva línea (`\n`):

`{{command}} | rargs -0 {{command}} {0}`
