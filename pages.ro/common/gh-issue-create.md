# gh issue

> Creați probleme GitHub într-un depozit din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_issue_create>

- Creați o nouă problemă împotriva depozitului curent interactiv:

`gh issue create`

- Creați o nouă problemă cu eticheta `bug” interactiv:

`gh issue create --label "{{bug}}"`

- Creați o nouă problemă interactiv și atribuiți-o utilizatorilor specificați:

`gh issue create --assignee {{user1,user2,...}}`

- Creați o nouă problemă cu un titlu, corp și atribuiți-o utilizatorului curent:

`gh issue create --title "{{title}}" --body "{{body}}" --assignee "{{@me}}"`

- Creați o nouă problemă interactiv, citind textul corpului dintr-un fișier:

`gh issue create --body-file {{path/to/file}}`

- Creați o nouă problemă în browserul web implicit:

`gh issue create --web`

- Afișează ajutorul:

`gh issue create --help`
