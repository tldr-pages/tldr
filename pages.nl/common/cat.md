# cat

> Toon en voeg bestanden samen.
> Meer informatie: <https://www.gnu.org/software/coreutils/cat>.

- Toon de inhoud van een bestand in `stdout`:

`cat {{pad/naar/bestand}}`

- Voeg verschillende bestanden samen in een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/uitvoerbestand}}`

- Voeg verschillende bestanden toe aan een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} >> {{pad/naar/uitvoerbestand}}`

- Kopieer de inhoud van een bestand in een uitvoerbestand zonder te bufferen:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Schrijf `stdin` naar een bestand:

`cat - > {{pad/naar/bestand}}`
