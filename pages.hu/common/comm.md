# comm

> Két fájl közös sorainak kiválasztása vagy elutasítása. Mindkét fájlnak rendezettnek kell lennie. További információ: <https://www.gnu.org/software/coreutils/comm>.

- Három tabulátorral elválasztott oszlopot állít elő: csak az első fájlban lévő sorok, csak a második fájlban lévő sorok és a közös sorok:

`comm {{file1}} {{file2}}`

- Csak a két fájlban közös sorok nyomtatása:

`comm -12 {{file1}} {{file2}}`

- Csak a két fájl közös sorainak nyomtatása, az egyik fájl beolvasása a `stdin`:

`cat {{file1}} | comm -12 - {{file2}}`

- Csak az első fájlban található sorok kinyerése, az eredményt egy harmadik fájlba mentve:

`comm -23 {{file1}} {{file2}} > {{file1_only}}`

- Csak a második fájlban talált sorok nyomtatása, ha a fájlok nincsenek rendezve:

`comm -13 <(sort {{file1}}) <(sort {{file2}})`
