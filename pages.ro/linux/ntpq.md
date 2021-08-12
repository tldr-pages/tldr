# ntpq

> Interogare demonul Network Time Protocol (NTP).
> Mai multe informaţii: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>

- Porniți `ntpq` în modul interactiv:

`ntpq --interactive`

- Imprimați o listă de colegi NTP:

`ntpq --peers`

- Imprimați o listă a colegilor NTP fără a rezolva numele de gazdă din adresele IP:

`ntpq --numeric --peers`

- Utilizați `ntpq` în modul de depanare:

`ntpq --debug-level`

- Imprimare valori ale variabilelor sistemului NTP:

`ntpq --command={{rv}}`
