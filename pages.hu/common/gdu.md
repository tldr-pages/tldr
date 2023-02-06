# gdu

> Lemezhasználati elemző konzolos felülettel. További információ: <https://github.com/dundee/gdu>.

- Interaktívan megjeleníti az aktuális könyvtár lemezhasználatát:

`gdu`

- Interaktívan megmutatja egy adott könyvtár lemezhasználatát:

`gdu {{path/to/directory}}`

- Interaktívan megmutatja az összes csatlakoztatott lemez lemez használatát:

`gdu --show-disks`

- Interaktívan megmutatja az aktuális könyvtár lemezhasználatát, de figyelmen kívül hagy néhány alkönyvtárat:

`gdu --ignore-dirs {{path/to/directory1,path/to/directory2,...}}`

- Az elérési utak figyelmen kívül hagyása szabályos kifejezéssel:

`gdu --ignore-dirs-pattern '{{.*[abc]+}}'`

- Rejtett könyvtárak figyelmen kívül hagyása:

`gdu --no-hidden`

- Csak az eredményt nyomtatja ki, nem lép interaktív módba:

`gdu --non-interactive {{path/to/directory}}`

- Nem interaktív módban ne jelenítse meg a folyamatot (hasznos szkriptekben):

`gdu --no-progress {{path/to/directory}}`
