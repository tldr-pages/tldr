# git restore

> Restura archivo del arbol de trabajo. Requiere la version 2.23 o superior de Git.
> Véase también `git checkout`
> Más información: <https://git-scm.com/docs/git-restore>.

- Restaura un archivo eliminado del contenido del commit actual (HEAD):

`git restore {{ruta/al/archivo}}`

- Restaura un archivo a la versión de un commit diferente:

`git restore --source {{commit}} {{ruta/al/archivo}}`

- Deshace cambios sin commit para los archivos rastreados, revirtiendo al HEAD actual:

`git restore .`
