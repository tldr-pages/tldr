# du

> Disk gebruik: schat en groepeer bestand en directory ruimte gebruik.
> Meer informatie: <https://ss64.com/osx/du.html>.

- Toont de grootte van een directory en mogelijke sub-directories, met een gegeven eenheid (KiB/MiB/GiB):

`du -{{k|m|g}} {{pad/naar/directory}}`

- Toont de grootte van een directory en mogelijke sub-directories, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h {{pad/naar/directory}}`

- Toont de grootte van een enkele directory met een leesbaar eenheid formaat:

`du -sh {{pad/naar/directory}}`

- Toont de grootte in leesbare vorm van een directory met alle bestanden en directories:

`du -ah {{pad/naar/directory}}`

- Toont de grootte in leesbare vorm van een directory en alle sub-directories tot N niveaus diep:

`du -h -d {{N}} {{pad/naar/directory}}`

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-directories van de huidige directory en laat een cumulatief totaal zien op het eind:

`du -ch {{*/*.jpg}}`
