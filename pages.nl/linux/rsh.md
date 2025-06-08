# rsh

> Voer commando's uit op een externe host.
> Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- Voer een commando uit op een externe host:

`rsh {{remote_host}} {{ls -l}}`

- Voer een commando uit op een externe host met een specifieke gebruikersnaam:

`rsh {{remote_host}} {{[-l|--user]}} {{gebruikersnaam}} {{ls -l}}`

- Redirect `stdin` naar `/dev/null` bij het uitvoeren van een commando op een externe host:

`rsh {{remote_host}} --no-err {{ls -l}}`
