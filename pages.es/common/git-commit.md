# git commit

> Realiza commits de los archivos al repositorio.
> Más información: <https://git-scm.com/docs/git-commit>.

- Raliza un commit de los archivos marcados al repositorio con un mensaje:

`git commit -m {{mensaje}`

- Marca automáticamente todos los archivos modificados y realiza un commit con un mensaje:

`git commit -a -m {{mensaje}}`

- Sustituye el último commit con los cambios marcados actualmente:

`git commit --amend`

- Realiza un commit para unos archivos específicos (que ya deben haber sido marcados previamente):

`git commit {{ruta/de/mi/archivo1}} {{ruta/de/mi/archivo2}}`
