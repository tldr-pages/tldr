# du

> Disk gebruik: schat en groepeer bestand en map ruimte gebruik.
> Meer informatie: <https://ss64.com/osx/du.html>.

- Toont de grootte van een map en mogelijke sub-mappen, met een gegeven eenheid (KiB/MiB/GiB):

`du -{{k|m|g}} {{pad/naar/map}}`

- Toont de grootte van een map en mogelijke sub-mappen, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h {{pad/naar/map}}`

- Toont de grootte van een enkele map met een leesbaar eenheid formaat:

`du -sh {{pad/naar/map}}`

- Toont de grootte in leesbare vorm van een map met alle bestanden en mappen:

`du -ah {{pad/naar/map}}`

- Toont de grootte in leesbare vorm van een map en alle sub-mappen tot N niveaus diep:

`du -h -d {{N}} {{pad/naar/map}}`

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-mappen van de huidige map en laat een cumulatief totaal zien op het eind:

`du -ch {{*/*.jpg}}`
