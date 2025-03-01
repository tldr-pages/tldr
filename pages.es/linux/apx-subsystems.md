# apx subsystems

> Administra subsistemas en `apx`.
> Los subsistemas son contenedores que pueden crearse a partir de stacks preexistentes.
> Más información: <https://github.com/Vanilla-OS/apx>.

- Crea de forma interactiva un nuevo subsistema:

`apx subsystems new`

- Muestra la lista de todos los subsistemas disponibles:

`apx subsystems list`

- Restablece un subsistema específico a su estado inicial:

`apx subsystems reset --name {{cadena_de_caracteres}}`

- Fuerza el restablecimiento de un subsistema específico:

`apx subsystems reset --name {{cadena_de_caracteres}} --force`

- Elimina un subsistema específico:

`apx subsystems rm --name {{cadena_de_caracteres}}`

- Fuerza la eliminación de un subsistema específico:

`apx subsystems rm --name {{cadena_de_caracteres}} --force`
