# shutdown

> Opriți și reporniți sistemul.

- Oprire (oprire) imediat:

`shutdown -h now`

- Reporniți imediat:

`shutdown -r now`

- Reporniți în 5 minute:

`shutdown -r +{{5}} &`

- Oprire la 1:00pm (Utilizează ceas 24h):

`shutdown -h 13:00`

- Anulați o operațiune de oprire/repornire în așteptare:

`shutdown -c`
