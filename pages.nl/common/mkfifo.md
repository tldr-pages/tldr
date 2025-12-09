# mkfifo

> Maak FIFOs (benoemde pipes).
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Maak een benoemde pipe op een opgegeven pad:

`mkfifo {{pad/naar/pipe}}`

- Stuur data naar een benoemde pipe en stuur het commando naar de achtergrond:

`echo "{{Hello World}}" > {{pad/naar/pipe}} &`

- Ontvang data van benoemde pipe:

`cat {{pad/naar/pipe}}`

- Deel je terminal sessie in real-time:

`mkfifo {{pad/naar/pipe}}; script {{[-f|--flush]}} {{pad/naar/pipe}}`
