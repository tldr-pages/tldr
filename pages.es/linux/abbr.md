# abbr

> Administra abreviaturas del intérprete de comandos fish.
> Las palabras definidas por el usuario se reemplazan con frases más largas después de ingresarlas.
> Más información: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Añade una nueva abreviatura:

`abbr --add {{nombre_abreviatura}} {{comando}} {{argumentos_del_comando}}`

- Cambia el nombre de una abreviatura existente:

`abbr --rename {{nombre_antiguo}} {{nombre_nuevo}}`

- Borra una abreviatura existente:

`abbr --erase {{nombre_abreviatura}}`

- Importa las abreviaturas definidas en otro host a través de SSH:

`ssh {{nombre_host}} abbr --show | source`
