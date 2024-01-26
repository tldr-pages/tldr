# rargs

> Ejecuta un comando por cada línea de entrada estándar.
> Similar a `xargs`, pero con soporte de coincidencia de patrones.
> Más información: <https://github.com/lotabout/rargs>.

- Ejecuta un comando por cada línea de entrada, como `xargs` (`{0}` indica donde sustituir en el texto):

`{{comando}} | rargs {{comando}} {0}`

- Imprime los comandos que se ejecutarían en vez de ejecutarlos:

`{{comando}} | rargs -e {{comando}} {0}`

- Elimina la extensión `.bak` de todos los archivos de una lista:

`{{comando}} | rargs -p '(.*).bak mv {0} {1}`

- Ejecuta comandos en paralelo:

`{{comando}} | rargs -w {{máxima_cantidad_de_procesos}}`

- Lee líneas de entrada separadas por el caracter `NUL` (`\0`) en vez de `LF` (`\n`):

`{{comando}} | rargs -0 {{comando}} {0}`
