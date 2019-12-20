# git remote

> Gestiona el conjunto de repositorios rastreados ("remotos").
> Más información: <https://git-scm.com/docs/git-remote>.

- Muestra una lista de los remotos existentes, sus nombres y URL:

`git remote -v`

- Añade un remoto:

`git remote add {{nombre_remoto}} {{url_remoto}}`

- Cambiar la URL de un remoto (utiliza `--add` para mantener la URL existente):

`git remote set-url {{nombre_remoto}} {{nueva_url}}`

- Elimina un remoto:

`git remote remove {{nombre_remoto}}`

- Renombra un remoto:

`git remote rename {{nombre_antiguo}} {{nombre_nuevo}}`
