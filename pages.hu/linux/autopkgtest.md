# autopkgtest

> Tesztek futtatása Debian csomagokon. További információ: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Építse a csomagot az aktuális könyvtárba, és futtassa az összes tesztet közvetlenül a rendszeren:

`autopkgtest -- {{null}}`

- Az aktuális könyvtárban lévő csomaghoz tartozó konkrét tesztek futtatása:

`autopkgtest --test-name={{test_name}} -- {{null}}`

- Egy adott csomag letöltése és összeállítása a `apt-get` segítségével, majd az összes teszt futtatása:

`autopkgtest {{package}} -- {{null}}`

- A csomag tesztelése az aktuális könyvtárban egy új gyökérkönyvtár segítségével:

`autopkgtest -- {{chroot}} {{path/to/new/root}}`

- A csomag tesztelése az aktuális könyvtárban anélkül, hogy újraépítené:

`autopkgtest --no-built-binaries -- {{null}}`
