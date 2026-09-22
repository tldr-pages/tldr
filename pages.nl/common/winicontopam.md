# winicontopam

> Converteer een Windows ICO bestand naar een PAM bestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- Lees een ICO bestand en converteer de beste kwaliteit afbeelding daarin naar het PAM formaat:

`winicontopam {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Converteer alle afbeeldingen in het invoerbestand naar PAM:

`winicontopam {{[-al|-allimages]}} {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Converteer de n'de afbeelding in het invoerbestand naar PAM:

`winicontopam {{[-i|-image]}} {{n}} {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Als de afbeelding(en) die geëxtraheerd moeten worden gegradeerde transparantiegegevens en een AND mask bevatten, schrijf de AND mask naar het vijfde kanaal van het PAM-uitvoerbestand:

`winicontopam {{[-an|-andmasks]}} {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`
