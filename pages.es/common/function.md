# function

> Define una función.
> Vea también: `declare`, `unset`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions>.

- Define una función con el nombre especificado:

`function {{nombre_funcion}} { {{echo "Contenido de la función aquí"}}; }`

- Ejecuta una función llamada `func_name`:

`func_name`

- Define una función sin la palabra clave `function`:

`{{func_name}}() { {{echo "Contenido de la función aquí"}}; }`

- Muestra la ayuda:

`help function`
