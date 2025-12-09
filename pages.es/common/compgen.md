# compgen

> Un comando incorporado para autocompletar en Bash, que es invocado al presionar la tecla `<Tab>` dos veces.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Lista todos los comandos que puedes ejecutar:

`compgen -c`

- Lista todos los comandos que puedes ejecutar y que comienzan con una cadena especificada:

`compgen -c {{str}}`

- Lista todos los alias:

`compgen -a`

- Lista todas las funciones que puedes ejecutar:

`compgen -A function`

- Muestra las palabras clave reservadas de la interfaz de comandos:

`compgen -k`

- Vea todos los comandos/alias disponibles que empiecen por `ls`:

`compgen -ac {{ls}}`

- Lista todos los usuarios del sistema:

`compgen -u`

- Muestra la ayuda:

`compgen --help`
