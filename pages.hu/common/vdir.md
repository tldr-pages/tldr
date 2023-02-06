# vdir

> A könyvtárak tartalmának listázása. A `ls -l` helyettesíthető. További információ: <https://www.gnu.org/software/coreutils/vdir>.

- Az aktuális könyvtárban lévő fájlok és könyvtárak felsorolása, soronként egyenként, részletekkel:

`vdir`

- Lista az ember által olvasható egységekben (KB, MB, GB) megjelenített méretekkel:

`vdir -h`

- Lista a rejtett fájlokkal (ponttal kezdődő):

`vdir -a`

- Fájlok és könyvtárak listája a bejegyzések méret szerinti rendezésével (a legnagyobb először):

`vdir -S`

- Fájlok és könyvtárak listája a módosítási idő szerint rendezve (a legfrissebb először):

`vdir -t`

- A könyvtárak csoportosítása elsőnek:

`vdir --group-directories-first`

- Egy adott könyvtár összes fájljának és könyvtárának rekurzív listázása:

`vdir --recursive {{path/to/directory}}`
