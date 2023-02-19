# abbr

> Administrar abreviaturas para el shell fish.
> Las palabras definidas por el usuario se reemplazan con frases más largas después de ingresarlas.
> Más información: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Añadir una nueva abreviatura:

`abbr --add {{nombre_abreviatura}} {{comando}} {{argumentos_del_comando}}`

- Cambiar el nombre de una abreviatura existente:

`abbr --rename {{nombre_antiguo}} {{nombre_nuevo}}`

- Borrar una abreviatura existente:

`abbr --erase {{nombre_abreviatura}}`

- Importar las abreviaturas definidas en otro host a través de SSH:

`ssh {{nombre_host}} abbr --show | source`
