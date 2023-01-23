# lerna

> Több csomagot tartalmazó JavaScript projektek kezelésére szolgáló eszköz. További információ: <https://lerna.js.org>.

- Projektfájlok inicializálása (`lerna.json`, `package.json`, `.git`, stb.):

`lerna init`

- Telepítse az egyes csomagok összes külső függőségét, és a helyi függőségek szimbolikus összekapcsolása:

`lerna bootstrap`

- Futtasson egy adott szkriptet minden olyan csomaghoz, amely tartalmazza a `package.json`:

`lerna run {{script}}`

- Egy tetszőleges shell parancs végrehajtása minden csomagban:

`lerna exec -- {{ls}}`

- Az összes olyan csomag közzététele, amely az utolsó kiadás óta megváltozott:

`lerna publish`
