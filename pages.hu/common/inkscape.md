# inkscape

> SVG (Scalable Vector Graphics) szerkesztő program. 0.92.x-ig az Inkscape verziókhoz használd a -e-t a -o helyett. További információ: <https://inkscape.org>.

- Nyisson meg egy SVG-fájlt az Inkscape felhasználói felületén:

`inkscape {{filename.svg}}`

- Exportáljon egy SVG-fájlt bitképbe az alapértelmezett formátumban (PNG) és az alapértelmezett felbontásban (96 DPI):

`inkscape {{filename.svg}} -o {{filename.png}}`

- Exportáljon egy SVG-fájlt 600x400 pixeles bittérképbe (a képarány torzulása előfordulhat):

`inkscape {{filename.svg}} -o {{filename.png}} -w {{600}} -h {{400}}`

- Egy SVG-fájl rajzának (az összes objektum határoló dobozának) exportálása bitképbe:

`inkscape {{filename.svg}} -o {{filename.png}} -D`

- Egyetlen objektum exportálása bitképbe, annak azonosítója alapján:

`inkscape {{filename.svg}} -i {{id}} -o {{object.png}}`

- SVG-dokumentum exportálása PDF-be, minden szöveget útvonallá alakítva:

`inkscape {{filename.svg}} -o {{filename.pdf}} --export-text-to-path`

- Az id="path123" objektum duplikálása, a duplikátum 90 fokos elforgatása, a fájl mentése és az Inkscape kilépése:

`inkscape {{filename.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
