# git diff

> A nyomon követett fájlok változásainak megjelenítése. További információ: <https://git-scm.com/docs/git-diff>.

- Szerkesztetlen, még el nem könyvelt változtatások megjelenítése:

`git diff`

- Az összes nem commitolt változtatás megjelenítése (beleértve a staged változásokat is):

`git diff HEAD`

- Csak a staged (hozzáadott, de még nem commitolt) változtatások megjelenítése:

`git diff --staged`

- Megjelenítheti az összes, egy adott dátum/idő (dátumkifejezés, pl. "1 hét 2 nap" vagy egy ISO dátum) óta végrehajtott változtatásokat:

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Csak az adott commit óta megváltoztatott fájlok neveinek megjelenítése:

`git diff --name-only {{commit}}`

- Az adott commit óta történt fájl-létrehozások, átnevezések és módváltozások összefoglalójának kiadása:

`git diff --summary {{commit}}`

- Egyetlen fájl összehasonlítása két ág vagy commit között:

`git diff {{branch_1}}..{{branch_2}} [--] {{path/to/file}}`

- Különböző fájlok összehasonlítása az aktuális ágból egy másik ággal:

`git diff {{branch}}:{{path/to/file2}} {{path/to/file}}`
