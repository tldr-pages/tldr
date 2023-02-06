# rg

> A Ripgrep egy rekurzív sor-orientált CLI keresőeszköz. Célja, hogy a `grep` gyorsabb alternatívája legyen. További információ: <https://github.com/BurntSushi/ripgrep>.

- Rekurzív keresés az aktuális könyvtárban egy reguláris kifejezésre:

`rg {{regular_expression}}`

- Rekurzívan keres reguláris kifejezésekre az aktuális könyvtárban, beleértve a rejtett és a `.gitignore` oldalon felsorolt fájlokat is:

`rg --no-ignore --hidden {{regular_expression}}`

- Csak egy bizonyos fájltípusban (pl. HTML, CSS stb.) keressen egy reguláris kifejezést:

`rg --type {{filetype}} {{regular_expression}}`

- Egy reguláris kifejezés keresése csak a könyvtárak egy részhalmazában:

`rg {{regular_expression}} {{set_of_subdirs}}`

- Egy reguláris kifejezés keresése egy globusnak megfelelő fájlokban (pl. `README.*`):

`rg {{regular_expression}} --glob {{glob}}`

- Csak az egyező fájlok listázása (hasznos, ha más parancsokhoz továbbítja):

`rg --files-with-matches {{regular_expression}}`

- A megadott reguláris kifejezésnek nem megfelelő sorok megjelenítése:

`rg --invert-match {{regular_expression}}`

- Szó szerinti karakterlánc-mintázat keresése:

`rg --fixed-strings -- {{string}}`
