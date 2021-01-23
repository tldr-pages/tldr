# git switch

> Alterna entre ramas Git. Requiere una Git 2.23+.
> Véase también `git-checkout`.
> Más información: <https://git-scm.com/docs/git-switch>.

- Cambia a una rama existente:

`git switch {{nombre_de_la_rama}}`

- Crea una nueva rama y se cambia a esta:

`git switch --create {{nombre_de_la_rama}}`

- Crea una nueva rama basada en un commit específico y se cambia a esta:

`git switch --create {{nombre_de_la_rama}} {{commit}}`

- Se cambia a una rama y actualiza todos los submódulos para coincidir:

`git switch --recurse-submodules {{nombre_de_la_rama}}`

- Se cambia a una rama y automáticamente fusiona la rama actual y cualquier cambio sin commit en ella:

`git switch --merge {{nombre_de_la_rama}}`
