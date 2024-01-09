# git stash

> Almacena los cambios locales de Git en un área temporal.
> Más información: <https://git-scm.com/docs/git-stash>.

- Almacena los cambios actuales, excepto los archivos nuevos (sin seguimiento):

`git stash push -m {{mensaje_opcional_stash}}`

- Almacena los cambios actuales, incluyendo los archivos nuevos (sin seguimiento):

`git stash -u`

- Selecciona interactivamente partes de los archivos modificados para almacenarlos:

`git stash -p`

- Lista todos los stashes (muestra el nombre del stash, la rama relacionada y el mensaje):

`git stash list`

- Muestra los cambios como un parche entre el stash (por defecto es `stash@{0}`) y la confirmación de cuando se creó la entrada stash por primera vez:

`git stash show -p {{stash@{0}}}`

- Aplica un stash (por defecto es el último, llamado `stash@{0}`):

`git stash apply {{nombre_opcional_del_stash_o_confirmación}}`

- Suelta o aplica un stash (por defecto es `stash@{0}`) y lo elimina de la lista de stash si su aplicación no causa conflictos:

`git stash pop {{nombre_opcional_stash}}`

- Elimina todos los stashes:

`git stash clear`
