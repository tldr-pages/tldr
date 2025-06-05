# complete

> Autocompleta argumentos para comandos de la interfaz interactiva (shell).
> Más información: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html#index-complete>.

- Aplica una función que realiza autocompletado a un comando:

`complete -F {{función}} {{comando}}`

- Aplica un comando que realiza autocompletado a otro comando:

`complete -C {{comando_de_autocompletado}} {{comando}}`

- Aplica autocompletado sin agregar espacio a la palabra completada:

`complete -o nospace -F {{función}} {{comando}}`
