# du

> Schijfgebruik: schat en vat ruimtegebruik van bestanden en mappen samen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Toon de grootte van een map en mogelijke sub-mappen, met een gegeven eenheid (B/KiB/MiB):

`du -{{b|k|m}} {{pad/naar/map}}`

- Toon de grootte van een map en mogelijke sub-mappen, met een leesbaar formaat (d.w.z. door het automatisch kiezen van een eenheid gebaseerd op grootte):

`du {{[-h|--human-readable]}} {{pad/naar/map}}`

- Toon de grootte van een enkele map met een leesbaar eenheid formaat:

`du {{[-sh|--summarize --human-readable]}} {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van een map met alle bestanden en mappen:

`du {{[-ah|--all --human-readable]}} {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van een map en alle sub-mappen tot `n` niveaus diep:

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} {{n}} {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van alle `.jpg` bestanden in de huidige map en laat een cumulatief totaal zien op het eind:

`du {{[-ch|--total --human-readable]}} *.jpg`

- Toon alle bestanden en mappen (inclusief verborgen) boven een bepaalde drempelwaarde (bruikbaar om te onderzoeken wat veel ruimte in neemt):

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`
