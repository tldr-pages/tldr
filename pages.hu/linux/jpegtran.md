# jpegtran

> JPEG fájlok veszteségmentes átalakítása. További információ: <https://manned.org/jpegtran>.

- Egy kép vízszintes vagy függőleges tükrözése:

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Egy kép elforgatása 90, 180 vagy 270 fokkal az óramutató járásával megegyező irányban:

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- A kép transzponálása a bal felső tengelyen át a jobb alsó tengelyre:

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- A kép átfordítása a jobb felső tengelyen a bal alsó tengelyre:

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- A kép szürkeárnyalatossá alakítása:

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- A képet a bal felső saroktól egy téglalap alakú, `W` szélességű és `H` magasságú régióra vágja, a kimenetet egy adott fájlba mentve:

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- A képet a `W` szélességű és a `H` magasságú téglalap alakú régióra vágja, a bal felső saroktól a `X` és a `Y` ponton kezdve:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`
