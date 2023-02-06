# codespell

> Helyesírás-ellenőrző a forráskódhoz. További információ: <https://github.com/codespell-project/codespell>.

- Az aktuális könyvtárban lévő összes szöveges fájlban rekurzívan ellenőrzi a helyesírási hibákat:

`codespell`

- Helyben talált összes helyesírási hiba kijavítása:

`codespell --write-changes`

- A megadott mintának megfelelő nevű fájlok kihagyása (a mintákat vesszővel elválasztott listát fogad el, a vadkártyák használatával):

`codespell --skip "{{pattern}}"`

- Egyéni szótárfájl használata az ellenőrzés során (`--dictionary` többször is használható):

`codespell --dictionary {{path/to/file.txt}}`

- Ne ellenőrizze a megadott fájlban szereplő szavakat:

`codespell --ignore-words {{path/to/file.txt}}`

- Ne ellenőrizze a megadott szavakat:

`codespell --ignore-words-list {{words,to,ignore}}`

- Minden egyes találat előtt vagy után 3 sor szövegkörnyezetet nyomtasson ki:

`codespell --{{context|before-context|after-context}} {{3}}`

- A fájlnevek ellenőrzése elgépelésekre, a fájl tartalmán kívül:

`codespell --check-filenames`
