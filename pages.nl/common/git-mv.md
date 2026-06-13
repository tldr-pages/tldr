# git mv

> Verplaats of hernoem bestanden en update de Git-index.
> Meer informatie: <https://git-scm.com/docs/git-mv>.

- Verplaats een bestand binnen de repository en voeg de verplaatsing toe aan de volgende commit:

`git mv {{pad/naar/bestand}} {{pad/naar/bestemming}}`

- Hernoem een bestand of map en voeg de hernoeming toe aan de volgende commit:

`git mv {{pad/naar/bestand_of_map}} {{pad/naar/bestemming}}`

- Overschrijf het bestand of de map op het doelpad als het bestaat:

`git mv {{[-f|--force]}} {{pad/naar/bestand_of_map}} {{pad/naar/bestemming}}`
