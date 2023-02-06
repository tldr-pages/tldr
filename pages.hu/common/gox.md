# gox

> Egy eszköz Go programok keresztkompilálására. További információ: <https://github.com/mitchellh/gox>.

- Go program fordítása az aktuális könyvtárban az összes operációs rendszer és architektúra kombinációjára:

`gox`

- Go program letöltése és lefordítása egy távoli URL-címről:

`gox {{url_1}} {{url_2}}`

- Kompilálja az aktuális könyvtárat egy adott operációs rendszerhez:

`gox -os="{{os}}"`

- Jelenlegi könyvtár fordítása egyetlen operációs rendszer és architektúra kombinációhoz:

`gox -osarch="{{os}}/{{arch}}"`
