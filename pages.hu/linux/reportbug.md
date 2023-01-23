# reportbug

> A Debian disztribúció hibabejelentő eszköze. További információ: <https://manpages.debian.org/latest/reportbug/reportbug.html>.

- Hibajelentést készíthet egy adott csomagról, majd elküldheti e-mailben:

`reportbug {{package}}`

- Olyan hiba jelentése, amely nem egy konkrét csomagról szól (általános probléma, infrastruktúra, stb.):

`reportbug other`

- Írja a hibajelentést egy fájlba ahelyett, hogy e-mailben küldené el:

`reportbug -o {{filename}} {{package}}`
