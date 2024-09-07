# mkfifo

> Maak FIFOs (benoemde pipes).
> Meer informatie: <https://www.gnu.org/software/coreutils/mkfifo>.

- Maak een benoemde pipe op een opgegeven pad:

`mkfifo {{pad/naar/pipe}}`

- Stuur data naar een benoemde pipe en stuur het commando naar de achtergrond:

`echo {{"Hello World"}} > {{pad/naar/pipe}} &`

- Ontvang data van benoemde pipe:

`cat {{pad/naar/pipe}}`
