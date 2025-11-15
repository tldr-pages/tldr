# complete

> Obtiene y establece las reglas de autocompletado de argumentos de los comandos del shell en Bash.
> Las terminaciones especificadas se invocarán cuando se pulse `<Tab>` en Bash.
> Vea también: `compgen`, `compopt`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-complete>.

- Establece los argumentos de un comando para autocompletar a través de una función (la respuesta de completado se envía en la variable `COMPREPLY`):

`complete -F {{función}} {{comando}}`

- Establece los argumentos de un comando para autocompletar a través de otro comando (`$1` es el comando, `$2` es el argumento sobre el que está el cursor y `$3` es el argumento que precede al cursor):

`complete -C {{comando_de_autocompletado}} {{comando}}`

- Configura los argumentos de un comando para que se autocompleten con los componentes del shell:

`complete -b {{comando}}`

- Aplica el autocompletado sin añadir un espacio a la palabra completada:

`complete -o nospace -F {{función}} {{comando}}`

- Lista todas las especificaciones completas cargadas:

`complete -p`

- Lista de especificaciones completas cargadas para un comando:

`complete -p {{comando}}`
