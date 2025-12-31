# git shortlog

> Resume la salida de `git log`.
> Más información: <https://git-scm.com/docs/git-shortlog>.

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas alfabéticamente por autor:

`git shortlog`

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas por el número de confirmaciones realizadas:

`git shortlog {{[-n|--numbered]}}`

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas por la identidad de quien realiza la confirmación (usuario y correo electrónico):

`git shortlog {{[-c|--committer]}}`

- Muestra un resumen de las últimas cinco confirmaciones (p. e., un rango de revisiones específico):

`git shortlog HEAD~5..HEAD`

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en la rama actual:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}}`

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en todas las ramas:

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}} --all`
