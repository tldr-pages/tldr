# crane auth

> Log in or access credentials.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>.

- Execute `crane auth` subcommand:

`crane auth {{subcommand}}`

- Implement credential helper:

`crane auth get {{registry_address}} {{[-h|--help]}}`

- Log in to a registry:

`crane auth login {{registry_address}} {{[-h|--help]}} {{[-p|--password]}} {{password}} {{-password-stdin}} {{[-u|--username]}} {{username}}`

- Log out of a registry:

`crane auth logout {{registry_address}} {{[-h|--help]}}`

- Retrieve a token for a remote repository:

`crane auth token {{registry_address}} {{[-H|--header]}} {{[-h|--help]}} {{[-m|--mount]}} {{scope1 scope2 ...}} --push`

- Display help:

`crane auth {{[-h|--help]}}`
