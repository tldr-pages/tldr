# git switch

> Alterna entre ramas Git. Requiere una versión 2.23+ de Git.
> Vea también `git checkout`.
> Más información: <https://git-scm.com/docs/git-switch>.

- Cambia a una rama existente:

`git switch {{nombre_de_la_rama}}`

- Crea una nueva rama y se cambia a esta:

`git switch --create {{nombre_de_la_rama}}`

- Crea y cambia a una nueva rama basada en una confirmación específica:

`git switch --create {{nombre_de_la_rama}} {{confirmación}}`

- Cambia a la rama anterior:

`git switch -`

- Cambia a una rama y actualiza todos los submódulos para coincidir:

`git switch --recurse-submodules {{nombre_de_la_rama}}`

- Cambia a una rama y automáticamente fusiona la rama actual y cualquier cambio sin confirmación en ella:

`git switch --merge {{nombre_de_la_rama}}`
