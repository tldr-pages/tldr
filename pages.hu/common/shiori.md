# shiori

> Egyszerű könyvjelző-kezelő Go segítségével. További információ: <https://github.com/go-shiori/shiori>.

- Könyvjelzők importálása HTML Netscape könyvjelző formátumú fájlból:

`shiori import {{path/to/bookmarks.html}}`

- A megadott URL mentése könyvjelzőként:

`shiori add {{url}}`

- A mentett könyvjelzők listázása:

`shiori print`

- A mentett könyvjelző megnyitása egy böngészőben:

`shiori open {{bookmark_id}}`

- A könyvjelzők kezelésére szolgáló webes felület elindítása a 8181-es porton:

`shiori serve --port {{8181}}`
