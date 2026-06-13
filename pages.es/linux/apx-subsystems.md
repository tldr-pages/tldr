# apx subsystems

> Administra subsistemas en `apx`.
> Los subsistemas son contenedores que pueden crearse a partir de stacks preexistentes.
> Más información: <https://docs.vanillaos.org/docs/en/apx-manpage#subsystems>.

- Crea de forma interactiva un nuevo subsistema:

`apx subsystems new`

- Muestra la lista de todos los subsistemas disponibles:

`apx subsystems list`

- Restablece un subsistema específico a su estado inicial:

`apx subsystems reset {{[-n|--name]}} {{cadena_de_caracteres}}`

- Fuerza el restablecimiento de un subsistema específico:

`apx subsystems reset {{[-n|--name]}} {{cadena_de_caracteres}} {{[-f|--force]}}`

- Elimina un subsistema específico:

`apx subsystems rm {{[-n|--name]}} {{cadena_de_caracteres}}`

- Fuerza la eliminación de un subsistema específico:

`apx subsystems rm {{[-n|--name]}} {{cadena_de_caracteres}} {{[-f|--force]}}`
