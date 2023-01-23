# tig

> Egy szöveges módú felület a Git-hez. További információ: <https://github.com/jonas/tig>.

- Megjeleníti a commitok sorrendjét az aktuális commit-tól kezdődően, fordított időrendi sorrendben:

`tig`

- Egy adott ág történetének megjelenítése:

`tig {{branch}}`

- Konkrét fájlok vagy könyvtárak előzményeinek megjelenítése:

`tig {{path1 path2 ...}}`

- Két hivatkozás (például ágak vagy címkék) közötti különbség megjelenítése:

`tig {{base_ref}}..{{compared_ref}}`

- Az összes ágból és tárolóból származó commitok megjelenítése:

`tig --all`

- Elindulás a rejtek nézetben, az összes mentett rejtekhely megjelenítése:

`tig stash`
