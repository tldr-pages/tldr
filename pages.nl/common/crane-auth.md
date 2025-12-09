# crane auth

> Log in of verkrijg inloggegevens.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>.

- Voer het `crane auth` subcommando uit:

`crane auth {{subcommando}}`

- Implementeer credential helper:

`crane auth get {{registry_adres}} {{[-h|--help]}}`

- Log in bij een registry:

`crane auth login {{registry_adres}} {{[-h|--help]}} {{[-p|--password]}} {{wachtwoord}} {{-password-stdin}} {{[-u|--username]}} {{gebruikersnaam}}`

- Log uit bij een registry:

`crane auth logout {{registry_adres}} {{[-h|--help]}}`

- Verkrijg een token voor een remote repository:

`crane auth token {{registry_adres}} {{[-H|--header]}} {{[-h|--help]}} {{[-m|--mount]}} {{scope1 scope2 ...}} --push`

- Toon de help:

`crane auth {{[-h|--help]}}`
