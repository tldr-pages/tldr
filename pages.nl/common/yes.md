# yes

> Iets herhaaldelijk uitvoeren.
> Deze opdracht wordt vaak gebruikt om ja te beantwoorden op elke prompt door installatieopdrachten (zoals `apt-get`).
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Toon herhaaldelijk "bericht":

`yes {{bericht}}`

- Toon herhaaldelijk "y":

`yes`

- Accepteer alles wat wordt gevraagd door het commando `apt-get`:

`yes | sudo apt-get install {{programma}}`

- Toon herhaaldelijk een nieuwe regel om altijd de standaard optie van een vraag te accepteren:

`yes ''`
