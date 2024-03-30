# winicontopam

> Converteer een Windows ICO bestand naar een PAM bestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- Lees een ICO bestand en converteer de beste kwaliteit afbeelding daarin naar het PAM formaat:

`winicontopam {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Converteer alle afbeeldingen in het invoerbestand naar PAM:

`winicontopam -allimages {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Converteer de n afbeelding in het invoerbestand naar PAM:

`winicontopam -image {{n}} {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`

- Als de afbeelding(en) voor te extraheren bevatten transparantie data en een AND mask, scrhijf de AND mask naar het vijfde kanaal van het uitvoer PAM bestand:

`winicontopam -andmasks {{pad/naar/invoer_bestand.ico}} > {{pad/naar/uitvoer.pam}}`
