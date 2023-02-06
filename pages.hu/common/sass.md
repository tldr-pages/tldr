# sass

> SCSS vagy Sass fájlokat alakít át CSS-re. További információ: <https://sass-lang.com/documentation/cli/dart-sass>.

- SCSS vagy Sass fájl átalakítása CSS-be és az eredmény kinyomtatása:

`sass {{inputfile.scss|inputfile.sass}}`

- Egy SCSS vagy Sass fájl átalakítása CSS-be és az eredmény mentése egy fájlba:

`sass {{inputfile.scss|inputfile.sass}} {{outputfile.css}}`

- SCSS vagy Sass fájl figyelése a változásokra és a CSS fájl kimenete vagy frissítése ugyanazzal a fájlnévvel:

`sass --watch {{inputfile.scss|inputfile.sass}}`

- SCSS vagy Sass fájl figyelése a változásokra és a CSS fájl kimenete vagy frissítése a megadott fájlnévvel:

`sass --watch {{inputfile.scss|inputfile.sass}}:{{outputfile.css}}`
