# check-support-status

> Identificați pachetele Debian instalate pentru care suportul a trebuit să fie limitat sau încheiat prematur.
> Mai multe informaţii: <https://manpages.debian.org/buster/debian-security-support/check-support-status.1.en.html>

- Afișați pachetele al căror suport este limitat, sa încheiat deja sau se va termina mai devreme decât sfârșitul de viață al distribuției:

`check-support-status`

- Afișează numai pachete a căror suport sa încheiat:

`check-support-status --type {{ended}}`

- Treci peste tipărirea unui titlu:

`check-support-status --no-heading`
