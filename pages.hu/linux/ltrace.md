# ltrace

> Egy folyamat dinamikus könyvtárhívásainak megjelenítése. További információ: <https://manned.org/ltrace>.

- Egy program bináris könyvtárhívásainak kinyomtatása (nyomon követése):

`ltrace ./{{program}}`

- Könyvtárhívások számolása. Kinyomtat egy praktikus összefoglalót az aljára:

`ltrace -c {{path/to/program}}`

- Nyomon követi a malloc és free hívásokat, kihagyja a libc által végzetteket:

`ltrace -e malloc+free-@libc.so* {{path/to/program}}`

- Terminal helyett fájlba írjon:

`ltrace -o {{file}} {{path/to/program}}`
