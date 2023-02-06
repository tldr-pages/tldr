# ebuild

> Alacsony szintű interfész a Gentoo Portage rendszerhez. További információ: <https://wiki.gentoo.org/wiki/Ebuild>.

- Létrehozza vagy frissítse a csomaglistát:

`ebuild {{path/to/file.ebuild}} manifest`

- Tisztítsa meg az ideiglenes build könyvtárakat a build fájlhoz:

`ebuild {{path/to/file.ebuild}} clean`

- Források lekérése, ha nem léteznek:

`ebuild {{path/to/file.ebuild}} fetch`

- A források kibontása egy ideiglenes építési könyvtárba:

`ebuild {{path/to/file.ebuild}} unpack`

- A kinyert források lefordítása:

`ebuild {{path/to/file.ebuild}} compile`

- A csomag telepítése egy ideiglenes telepítési könyvtárba:

`ebuild {{path/to/file.ebuild}} install`

- Az ideiglenes fájlok telepítése az éles fájlrendszerbe:

`ebuild {{path/to/file.ebuild}} qmerge`

- A megadott ebuild fájl lekérése, kicsomagolása, lefordítása, telepítése és qmerge-je:

`ebuild {{path/to/file.ebuild}} merge`
