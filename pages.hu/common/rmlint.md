# rmlint

> Duplikált fájlok vagy könyvtárak és egyéb fájlrendszeri problémák azonosítása. További információ: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Egy könyvtár ellenőrzése duplikátumok, üres fájlok és egyéb problémák szempontjából:

`rmlint {{path/to/directory}}`

- A `rmlint` parancs végrehajtása során talált duplikált fájlok törlése:

`./rmlint.sh`

- Duplikált könyvtárfák keresése:

`rmlint --merge-directories {{path/to/directory}}`

- Jelölje meg az alacsonyabb elérési útvonal \[d\]epthoz tartozó fájlokat eredetinek:

`rmlint --rank-by={{d}} {{path/to/directory}}`

- A legrövidebb nevű fájlok \[l\]ength eredetinek jelölése:

`rmlint --rank-by={{l}} {{path/to/directory}}`

- Csak olyan duplikátumokat találjon, amelyeknek a tartalma mellett ugyanaz a fájlnév is megegyezik:

`rmlint --match-basename {{path/to/directory}}`

- Minden olyan duplikátum keresése, amelynek azonos a kiterjesztése:

`rmlint --match-extension {{path/to/directory}}`
