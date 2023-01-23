# f3write

> Töltsön meg egy meghajtót .h2w fájlokkal, hogy tesztelje annak valós kapacitását. Lásd még: `f3read`, `f3probe`, `f3fix`. További információ: <http://oss.digirati.com.br/f3/>.

- Tesztfájlok írása egy adott könyvtárba, a meghajtó feltöltésével:

`f3write {{path/to/mount_point}}`

- Korlátozza az írási sebességet:

`f3write --max-write-rate={{kb_per_second}} {{path/to/mount_point}}`
