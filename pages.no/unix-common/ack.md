# ack

> Et søkeverktøy som grep, optimalisert for utviklere.
> Se også: `rg`, som er mye raskere.
> Mer informasjon: <https://beyondgrep.com/documentation>.

- Søk etter filer som inneholder en streng eller regulært uttrykk i gjeldende katalog rekursivt:

`ack "{{søkemønster}}"`

- Søk etter et mønster som ikke skiller mellom store og små bokstaver:

`ack --ignore-case "{{søkemønster}}"`

- Søk etter linjer som samsvarer med et mønster, skriv ut bare den samsvarende teksten og ikke resten av linjen:

`ack -o "{{søkemønster}}"`

- Begrens søket til filer av en bestemt type:

`ack --type {{ruby}} "{{søkemønster}}"`

- Ikke søk i filer av en bestemt type:

`ack --type no{{ruby}} "{{søkemønster}}"`

- Tell totalt antall treff funnet:

`ack --count --no-filename "{{søkemønster}}"`

- Skriv ut filnavnene og antall treff kun for hver fil:

`ack --count --files-with-matches "{{søkemønster}}"`

- List opp alle verdiene som kan brukes med  `--type`:

`ack --help-types`
