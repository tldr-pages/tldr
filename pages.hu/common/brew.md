# brew

> Csomagkezelő macOS-hez és Linuxhoz. További információ: <https://brew.sh>.

- Telepítse a formula vagy a hordó legújabb stabil verzióját (a fejlesztői verziókhoz használja a `--devel` címet):

`brew install {{formula}}`

- Az összes telepített formula és hordó listája:

`brew list`

- Egy telepített formula vagy hordó frissítése (ha nincs megadva, az összes telepített formula/hordó frissül):

`brew upgrade {{formula}}`

- A Homebrew és az összes formula és hordó legújabb verziójának lekérdezése a Homebrew forrástárból:

`brew update`

- Megjeleníti azokat a formulákat és hordókat, amelyeknek újabb verziója érhető el:

`brew outdated`

- Elérhető formulák (azaz csomagok) és hordók (azaz natív csomagok) keresése:

`brew search {{text}}`

- Információk megjelenítése egy formuláról vagy hordóról (verzió, telepítési útvonal, függőségek stb.):

`brew info {{formula}}`

- A helyi Homebrew telepítés ellenőrzése az esetleges problémákra:

`brew doctor`
