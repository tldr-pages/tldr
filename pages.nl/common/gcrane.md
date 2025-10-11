# gcrane

> Beheer tool voor containerafbeeldingen.
> Deze tool implementeert een superset van de `crane`-commando's, met aanvullende commando's die specifiek zijn voor Google Container Registry (`gcr.io`).
> Sommige subcommando's zoals `append`, `auth`, `copy`, enz. hebben hun eigen gebruiksdocumentatie die te vinden is onder `crane`.
> Sommige subcommando's zoals `completion`, `gc`, `help` zijn specifiek voor gcrane en hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Log in op een register:

`gcrane auth login {{register}} {{[-u|--username]}} {{gebruiker}} {{[-p|--password]}} {{wachtwoord}}`

- Toon tags, manifesten en sub-repositories:

`gcrane ls {{register}}/{{project_id}}`

- Kopieer images van een register naar een andere:

`gcrane cp {{[-r|--recursive]}} {{bronregister}}/{{project_id}}/{{repository}} {{doelregister}}/{{project_id}}/{{repository}}`

- Toon images die door de garbage collecter verzameld kunnen worden:

`gcrane gc {{register}}/{{project_id}}/{{repository}}`

- Verwijder images die door de garbage collecter verzameld kunnen worden:

`gcrane gc {{register}}/{{project_id}}/{{repository}} | xargs {{[-n|--max-args]}} 1 gcrane delete`

- Toon een specifiek register met een specifieke ID:

`gcrane ls {{gcr.io}}/{{mijn-project-id}}`

- Migreer alle images van het VS-register naar het EU-register:

`gcrane cp {{[-r|--recursive]}} {{gcr.io}}/{{mijn-project-id}}/{{repository}} {{eu.gcr.io}}/{{mijn-project-id}}/{{repository}}`
