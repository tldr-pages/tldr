# git-imerge

> Ejecuta una fusión o rebase entre dos ramas Git incrementalmente.
> Los conflictos entre las ramas se rastrean a pares de commits individuales para simplificar la resolución de conflictos.
> Más información: <https://github.com/mhagger/git-imerge>.

- Inicia un rebase de tipo imerge (primero comprueba la rama a ser rebasada):

`git imerge rebase {{rama_a_rebasar}}`

- Inicia una fusión de tipo imerge (primero comprueba la rama en la que fusionar):

`git imerge merge {{rama_a_fusionar}}`

- Muestra una diagrama ASCII para la fusión o rebase en proceso:

`git imerge diagram`

- Continua la operación imerge después de resolver los conflictos (primero añade con `git add` los archivos conflictivos):

`git imerge continue --no-edit`

- Concluye una operación imerge después de que todos los conflictos se hayan resuelto:

`git imerge finish`

- Aborta una operación imerge y vuelve a la rama anterior:

`git-imerge remove && git checkout {{rama_anterior}}`
