# sdelete

> Verwijder veilig een bestand/map van de schijf, of maak de vrije ruimte op een volume/fysieke schijf schoon.
> Meer informatie: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- Verwijder bestanden met 3 [p]asses:

`sdelete -p 3 {{pad\naar\bestand1 pad\naar\bestand2 ...}}`

- Verwijder mappen en de [s]ubmappen met 1 pass (default):

`sdelete -s {{pad\naar\map1 pad\naar\map2 ...}}`

- Maak de vrije ruimte schoon van volume D: met 3 [p]asses:

`sdelete -p 3 D:`

- Maak de vrije ruimte schoon met nullen ([z]) van fysieke schijf 2, welke geen volumes meer mag bevatten die opgeschoond kunnen worden:

`sdelete -z 2`
