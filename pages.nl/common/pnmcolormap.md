# pnmcolormap

> Maak een kwantisatiekleurkaart voor een PNM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Genereer een afbeelding met alleen `n_kleuren` of minder kleuren, zo dicht als mogelijk bij de invoer-afbeelding:

`pnmcolormap {{n_kleuren}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.ppm}}`

- Gebruik de splitspread strategie voor het bepalen van de uitvoer-kleuren, welke waarschijnlijk een beter resultaat oplevert met afbeeldingen met kleine details:

`pnmcolormap -splitspread {{n_kleuren}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.ppm}}`

- Sorteer de resulteerde kleurkaart, welke nuttig is voor het vergelijken van kleurkaarten:

`pnmcolormap -sort {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.ppm}}`
