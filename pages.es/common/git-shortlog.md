# git shortlog

> Resume la salida de `git log`.
> Más información: <https://git-scm.com/docs/git-shortlog>.

- Muestra un resumen de todos los commits realizados, agrupados alfabéticamente por autor:

`git shortlog`

- Muestra un resumen de todos los commits realizados, agrupados por el número de commits realizados:

`git shortlog -n`

- Muestra un resumen de todos los commits realizados, agrupados por la identidad de quien realiza el commit (usuario y correo electrónico):

`git shortlog -c`

- Muestra un resumen de los últimos 5 commits (i. e., un rango de revisiones específico):

`git shortlog HEAD~{{5}}..HEAD`

- Muestra todos los usuarios, correos electrónicos y número de commits en la rama actual:

`git shortlog -sne`

- Muestra todos los usuarios, correos electrónicos y número de commits en todas las ramas:

`git shortlog -sne --all`
