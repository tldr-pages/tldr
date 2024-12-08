# complete

> Autocompleta argumentos para comandos de la interfaz interactiva (shell).
> Más información: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- Aplica una función que realiza auto completado a un comando:

`complete -F {{función}} {{comando}}`

- Aplica un comando que realiza auto completado a otro comando:

`complete -C {{comando_de_autocompletado}} {{comando}}`

- Aplica auto completado sin agregar espacio a la palabra completada:

`complete -o nospace -F {{función}} {{comando}}`
