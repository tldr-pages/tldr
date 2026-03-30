# git stash

> Guarda los cambios locales de Git en un área temporal.
> Más información: <https://git-scm.com/docs/git-stash>.

- Guarda los cambios actuales con un mensaje, excepto archivos nuevos (sin seguimiento):

`git stash push {{[-m|--message]}} {{mensaje_stash}}`

- Guarda los cambios actuales, incluyendo archivos nuevos sin seguimiento:

`git stash {{[-u|--include-untracked]}}`

- Selecciona interactivamente partes de los archivos modificados para guardar:

`git stash {{[-p|--patch]}}`

- Lista todos los stashes (muestra el nombre, la rama relacionada y el mensaje):

`git stash list`

- Muestra los cambios como un parche entre el stash (por defecto `stash@{0}`) y el commit en el que se creó la entrada del stash:

`git stash show {{[-p|--patch]}} {{stash@{0}}}`

- Aplica un stash (por defecto el más reciente, llamado `stash@{0}`):

`git stash apply {{nombre_stash_o_commit_opcional}}`

- Aplica un stash (por defecto `stash@{0}`) y lo elimina de la lista si no hay conflictos:

`git stash pop {{nombre_stash_opcional}}`

- Elimina todos los stashes:

`git stash clear`
