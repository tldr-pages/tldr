# rexec

> Voer een commando uit op een externe host.
> Let op: Gebruik `rexec` met voorzichtigheid, omdat het gegevens in platte tekst verzendt. Overweeg veilige alternatieven zoals SSH voor versleutelde communicatie.
> Meer informatie: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rexec-invocation>.

- Voer een commando uit op een externe [h]ost:

`rexec {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- Specificeer de externe [g]ebruikersnaam op een externe [h]ost:

`rexec {{[-u|--username]}} {{gebruikersnaam}} {{[-h|--host]}} {{remote_host}} {{ps aux}}`

- Redirect `stdin` van `/dev/null` op een externe [h]ost:

`rexec {{[-n|--noerr]}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- Specificeer de externe [P]oort op een externe [h]ost:

`rexec {{[-P|--port]}} {{1234}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`
