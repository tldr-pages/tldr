# pnmquant

> Kwantiseer de kleuren in een PNM afbeelding naar een kleinere set.
> Dit commando is een combinatie van `pnmcolormap` en `pnmremap` en accepteert de combinatie van hun opties, behalve `-mapfile`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Genereer een afbeelding door alleen gebruik te maken van `n_kleuren` of minder kleuren zo dichtbij mogelijk van de invoerafbeelding:

`pnmquant {{n_kleuren}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`
