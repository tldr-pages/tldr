# docker login

> Bei einer Docker Registry einloggen.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/login/>.

- Interaktives Einloggen bei einer Registry:

`docker login`

- Einloggen mit einem angegebenen Benutzernamen (fragt nach dem Passwort):

`docker login --username {{benutzername}}`

- Einloggen mit einem angegebenen Benutzernamen und Passwort:

`docker login --username {{benutzername}} --password {{passwort}} {{server}}`

- Einloggen mit einem Passwort, welches von `stdin` gelesen wird:

`echo "{{passwort}}" | docker login --username {{benutzername}} --password-stdin`
