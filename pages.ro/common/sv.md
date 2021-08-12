# sv

> Controlați un serviciu runsv care rulează.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/latest/man8/sv.8.html>

- Începe un serviciu:

`sudo sv up {{path/to/service}}`

- Opreşte un serviciu:

`sudo sv down {{path/to/service}}`

- Obțineți starea serviciului:

`sudo sv status {{path/to/service}}`

- Reîncarcă un serviciu:

`sudo sv reload {{path/to/service}}`

- Porniți un serviciu, dar numai dacă nu rulează și nu îl reporniți dacă se oprește:

`sudo sv once {{path/to/service}}`
