# gh release

> Gestionare versiuni GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_release>

- Lista de versiuni într-un depozit GitHub, limitat la 30 de articole:

`gh release list`

- Afișați informații despre o anumită versiune:

`gh release view {{tag}}`

- Creați o nouă versiune:

`gh release create {{tag}}`

- Ștergeți o anumită versiune:

`gh release delete {{tag}}`

- Descărcați active dintr-o anumită versiune:

`gh release download {{tag}}`

- Încărcați active într-o anumită versiune:

`gh release upload {{tag}} {{path/to/file1}} {{path/to/file2}}`
