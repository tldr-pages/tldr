# gcrane

> Beheertool voor containerafbeeldingen.
> Deze tool implementeert een superset van de `crane`-commando's, met aanvullende commando's die specifiek zijn voor Google Container Registry (`gcr.io`).
> Sommige subcommando's zoals `copy`, `gc`, `help`, `ls`, etc. hebben hun eigen documentatie.
> Zie ook: `crane`.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Log in op een registry:

`gcrane auth login {{registry}} {{[-u|--username]}} {{gebruiker}} {{[-p|--password]}} {{wachtwoord}}`

- Toon tags, manifesten en sub-repositories:

`gcrane ls {{registry}}/{{project_id}}`

- Kopieer images van een registry naar een andere:

`gcrane cp {{[-r|--recursive]}} {{bronregistry}}/{{project_id}}/{{repository}} {{doelregistry}}/{{project_id}}/{{repository}}`

- Toon images die door de garbage collector verzameld kunnen worden:

`gcrane gc {{registry}}/{{project_id}}/{{repository}}`

- Verwijder images die door de garbage collector verzameld kunnen worden:

`gcrane gc {{registry}}/{{project_id}}/{{repository}} | xargs {{[-n|--max-args]}} 1 gcrane delete`

- Toon een specifieke registry met een specifieke ID:

`gcrane ls {{gcr.io}}/{{mijn-project-id}}`

- Migreer alle images van de VS-registry naar de EU-registry:

`gcrane cp {{[-r|--recursive]}} {{gcr.io}}/{{mijn-project-id}}/{{repository}} {{eu.gcr.io}}/{{mijn-project-id}}/{{repository}}`
