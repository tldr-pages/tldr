# git remote

> Gestiona el conjunto de repositorios rastreados ("remotos").
> Más información: <https://git-scm.com/docs/git-remote>.

- Muestra una lista de los remotos existentes, sus nombres y URL:

`git remote -v`

- Añade un remoto:

`git remote add {{remote_name}} {{remote_url}}`

- Cambiar la URL de un remoto (utiliza `--add` para mantener la URL existente):

`git remote set-url {{remote_name}} {{new_url}}`

- Elimina un remoto:

`git remote remove {{remote_name}}`

- Renombra un remoto:

`git remote rename {{old_name}} {{new_name}}`
