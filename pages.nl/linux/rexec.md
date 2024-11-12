# rexec

> Voer een commando uit op een externe host.
> Let op: Gebruik `rexec` met voorzichtigheid, omdat het gegevens in platte tekst verzendt. Overweeg veilige alternatieven zoals SSH voor versleutelde communicatie.
> Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- Voer een commando uit op een externe [h]ost:

`rexec -h={{remote_host}} {{ls -l}}`

- Specificeer de externe [g]ebruikersnaam op een externe [h]ost:

`rexec -username={{gebruikersnaam}} -h={{remote_host}} {{ps aux}}`

- Redirect `stdin` van `/dev/null` op een externe [h]ost:

`rexec --no-err -h={{remote_host}} {{ls -l}}`

- Specificeer de externe [P]oort op een externe [h]ost:

`rexec -P={{1234}} -h={{remote_host}} {{ls -l}}`
