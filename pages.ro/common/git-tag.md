# git tag

> Creați, listați, ștergeți sau verificați etichetele.
> O etichetă este o referință statică la o anumită comitere.
> Mai multe informaţii: <https://git-scm.com/docs/git-tag>

- Listează toate etichetele:

`git tag`

- Creați o etichetă cu numele dat indicând spre comiterea curentă:

`git tag {{tag_name}}`

- Creați o etichetă cu numele dat indicând spre o anumită comitere:

`git tag {{tag_name}} {{commit}}`

- Creați o etichetă adnotată cu mesajul dat:

`git tag {{tag_name}} -m {{tag_message}}`

- Ștergeți eticheta cu numele dat:

`git tag -d {{tag_name}}`

- Obțineți etichete actualizate din amonte:

`git fetch --tags`

- Listează toate etichetele ale căror strămoși includ o anumită comită

`git tag --contains {{commit}}`
