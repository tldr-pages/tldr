# docker login

> Bei einer Docker Registry einloggen.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/login/>.

- Interaktives Einloggen bei einer Registry:

`docker login`

- Einloggen mit einem angegebenen Benutzernamen (fragt nach dem Passwort):

`docker login {{[-u|--username]}} {{benutzername}}`

- Einloggen mit einem angegebenen Benutzernamen und Passwort:

`docker login {{[-u|--username]}} {{benutzername}} {{[-p|--password]}} {{passwort}} {{server}}`

- Einloggen mit einem Passwort, welches von `stdin` gelesen wird:

`echo "{{passwort}}" | docker login {{[-u|--username]}} {{benutzername}} --password-stdin`
