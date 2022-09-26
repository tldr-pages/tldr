# env

> Vis miljøet eller kjør et program i et modifisert miljø.
> Mer informasjon: <https://www.gnu.org/software/coreutils/env>.

- Vis miljøet:

`env`

- Kjør et program. Ofte brukt i skript etter shebang (#!) for å slå opp stien til programmet:

`env {{program}}`

- Slett miljøet og kjør et program:

`env -i {{program}}`

- Fjern variabel fra miljøet og kjør et program:

`env -u {{variabel}} {{program}}`

- Angi en variabel og kjør et program:

`env {{variabel}}={{verdi}} {{program}}`

- Angi flere variabler og kjør et program:

`env {{variabel1}}={{verdi}} {{variabel2}}={{verdi}} {{variabel3}}={{verdi}} {{program}}`
