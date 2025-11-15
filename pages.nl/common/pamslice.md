# pamslice

> Haal een regel van waarden uit een PAM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Toon de waarden van de pixels in de opgegeven rij in een tabel:

`pamslice {{[-r|-row]}} {{n}} {{pad/naar/afbeelding.pam}}`

- Toon de waarden van de pixels in de opgegeven kolom in een tabel:

`pamslice {{[-c|-column]}} {{n}} {{pad/naar/afbeelding.pam}}`

- Beschouw alleen het opgegeven vlak (m) van de invoer-afbeelding:

`pamslice {{[-r|-row]}} {{n}} -plane {{m}} {{pad/naar/afbeelding.pam}}`

- Produceer uitvoer in een formaat dat geschikt is voor invoer naar een `xmgr` voor visualisatie:

`pamslice {{[-r|-row]}} {{n}} {{[-x|-xmgr]}} {{pad/naar/afbeelding.pam}}`
