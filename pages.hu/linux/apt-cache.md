# apt-cache

> Debian és Ubuntu csomaglekérdező eszköz. További információ: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Keressen egy csomagot az aktuális forrásaiban:

`apt-cache search {{query}}`

- Információk megjelenítése egy csomagról:

`apt-cache show {{package}}`

- Megmutatja, hogy egy csomag telepítve van-e és naprakész-e:

`apt-cache policy {{package}}`

- Egy csomag függőségi viszonyainak megjelenítése:

`apt-cache depends {{package}}`

- Az adott csomagtól függő csomagok megjelenítése:

`apt-cache rdepends {{package}}`
