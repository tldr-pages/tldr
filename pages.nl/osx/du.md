# du

> Schijfgebruik: schat en vat ruimtegebruik van bestanden en mappen samen.
> Meer informatie: <https://keith.github.io/xcode-man-pages/du.1.html>.

- Toon de grootte van een map en mogelijke sub-mappen, met een gegeven eenheid (KiB/MiB/GiB):

`du -{{k|m|g}} {{pad/naar/map}}`

- Toon de grootte van een map en mogelijke sub-mappen, met een leesbaar formaat (d.w.z. door het automatisch kiezen van een eenheid gebaseerd op grootte):

`du -h {{pad/naar/map}}`

- Toon de grootte van een enkele map met een leesbaar eenheid formaat:

`du -sh {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van een map met alle bestanden en mappen:

`du -ah {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van een map en alle sub-mappen tot `n` niveaus diep:

`du -h -d {{n}} {{pad/naar/map}}`

- Toon de grootte in leesbare vorm van alle `.jpg` bestanden in sub-mappen van de huidige map en laat een cumulatief totaal zien op het eind:

`du -ch */*.jpg`
