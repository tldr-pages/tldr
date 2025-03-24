# cat

> Print en concateneer bestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Print de inhoud van een bestand naar `stdout`:

`cat {{pad/naar/bestand}}`

- Concateneer meerdere bestanden in een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/uitvoerbestand}}`

- Voeg meerdere bestanden toe aan een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} >> {{pad/naar/uitvoerbestand}}`

- Schrijf `stdin` naar een bestand:

`cat - > {{pad/naar/bestand}}`

- [n]ummer alle uitvoerregels:

`cat {{[-n|--number]}} {{pad/naar/bestand}}`

- Toon niet-afdrukbare en witruimtekarakters (met `M-` prefix als niet-ASCII):

`cat {{[-vte|--show-nonprinting -t -e]}} {{pad/naar/bestand}}`
