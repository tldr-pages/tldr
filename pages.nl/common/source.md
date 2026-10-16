# source

> Voer opdrachten uit vanuit een bestand in de huidige shell.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-source>.

- Evalueer de inhoud van een bepaald bestand:

`source {{pad/naar/bestand}}`

- Evalueer een bestand met argumenten:

`source {{pad/naar/bestand}} {{argument1 argument2 ...}}`

- Zoek en evalueer een bestand uit `$PATH`:

`source {{bestand}}`

- Zoek en evalueer een bestand in een gegeven verzameling mappen:

`source -p {{pad/naar/map1:pad/naar/map2:...}} {{bestand}}`

- Evalueer de inhoud van een bepaald bestand (als alternatief ter vervanging van `source` door `.`):

`. {{pad/naar/bestand}}`
