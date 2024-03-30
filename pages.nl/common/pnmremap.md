# pnmremap

> Vervang de kleuren in een PNM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- Vervang de kleuren in een afbeelding met diegene gespecificeerd in een kleurenpalet:

`pnmremap -mapfile {{pad/naar/kleurenpalet_bestand.ppm}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Gebruik Floyd-Steinberg dithering voor het representeren van missende kleuren in het kleurenpalet:

`pnmremap -mapfile {{pad/naar/kleurenpalet_bestand.ppm}} -floyd {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Gebruik de eerste kleur in het palet voor het representeren van missende kleuren in het kleurenpalet:

`pnmremap -mapfile {{pad/naar/kleurenpalet_bestand.ppm}} -firstisdefault {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Gebruik de gespecificeerde kleur voor het representeren van de missende kleuren in het kleurenpalet:

`pnmremap -mapfile {{pad/naar/kleurenpalet_bestand.ppm}} -missingcolor {{kleur}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`
