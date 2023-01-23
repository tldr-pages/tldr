# pt

> Platinum Searcher. A `ag`-hoz hasonló kódkereső eszköz. További információ: <https://github.com/monochromegane/the_platinum_searcher>.

- A "foo" szót tartalmazó fájlok keresése és a kiemelt találatokkal rendelkező fájlok kinyomtatása:

`pt {{foo}}`

- A "foo" szót tartalmazó fájlok keresése és az egyes fájlokban található találatok számának megjelenítése:

`pt -c {{foo}}`

- A "foo"-t tartalmazó fájlok keresése egész szóval, és a nagy- és kisbetűs írásmód figyelmen kívül hagyása:

`pt -wi {{foo}}`

- "foo" keresése adott kiterjesztésű fájlokban reguláris kifejezéssel:

`pt -G='{{\.bar$}}' {{foo}}`

- Olyan fájlok keresése, amelyek tartalma megfelel a reguláris kifejezésnek, legfeljebb 2 könyvtár mélységig:

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`
