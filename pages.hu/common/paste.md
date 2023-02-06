# paste

> Fájlok sorainak egyesítése. További információ: <https://www.gnu.org/software/coreutils/paste>.

- Az összes sort egyetlen sorba illeszti, TAB-jelet használva elválasztójelként:

`paste -s {{path/to/file}}`

- Az összes sort egyetlen sorba egyesíti a megadott elválasztójel használatával:

`paste -s -d {{delimiter}} {{path/to/file}}`

- Két fájl egyesítése egymás mellé, mindegyik a saját oszlopában, TAB-ot használva elválasztójelként:

`paste {{file1}} {{file2}}`

- Két fájl egymás melletti egyesítése, mindegyik a saját oszlopában, a megadott elválasztójel használatával:

`paste -d {{delimiter}} {{file1}} {{file2}}`

- Két fájl összevonása, sorok felváltva történő hozzáadásával:

`paste -d '\n' {{file1}} {{file2}}`
