# git stash

> Guarda cambios locales de Git en un área temporal.
> Más información: <https://git-scm.com/docs/git-stash>.

- Guarda cambios actuales, excepto los archivos nuevos (sin rastrear):

`git stash [push -m {{mensaje_opcional_del_guardado}}]`

- Guarda cambios actuales, incluyendo los archivos nuevos (sin rastrear):

`git stash -u`

- Selecciona interactivamente las partes de archivos cambiados que deben ser guardadas:

`git stash -p`

- Muestra todos los guardados (muestra el nombre del guardado, la rama relacionada y el mensaje):

`git stash list`

- Aplica un guardado (por defecto aplica el último, llamado stash@{0}):

`git stash apply {{nombre_opcional_del_guardado_o_commit}}`

- Aplica un guardado (por defecto es stash@{0} y lo traslada desde la lista de guardado si no causa conflictos:

`git stash pop {{nombre_opcional_del_guardado}}`

- Elimina un guardado (por defecto es stash@{0}):

`git stash drop {{nombre_opcional_del_guardado}}`

- Elimina todos los guardados:

`git stash clear`
