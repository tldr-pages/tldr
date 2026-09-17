# compgen

> Comando integrado de Bash para generar posibles coincidencias de finalización en Bash.
> Se utiliza normalmente en funciones de finalización personalizadas.
> Vea también: `complete`, `compopt`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Enumera todos los comandos integrados, alias, funciones y ejecutables del intérprete de comandos que se pueden ejecutar:

`compgen -c`

- Enumera todos los comandos que puede ejecutar que comienzan con una cadena específica y guarda los resultados en `$COMPREPLY`:

`compgen -V COMPREPLY -c {{str}}`

- Compara con una lista de palabras:

`compgen -W "{{apple orange banana}}" {{a}}`

- Enumera todos los alias:

`compgen -a`

- Enumera todas las funciones que se pueden ejecutar:

`compgen -A function`

- Muestra las palabras clave reservadas del shell:

`compgen -k`

- Vea todos los comandos/alias disponibles que comienzan por `ls`:

`compgen -ac {{ls}}`

- Enumera todos los usuarios del sistema:

`compgen -u`
