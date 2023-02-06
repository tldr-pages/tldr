# open

> Megnyitja a fájlokat, könyvtárakat és alkalmazásokat. További információ: <https://ss64.com/osx/open.html>.

- Megnyit egy fájlt a hozzá tartozó alkalmazással:

`open {{file.ext}}`

- Grafikus macOS \[a\]pplikáció futtatása:

`open -a "{{Application}}"`

- Grafikus macOS-alkalmazás futtatása a \[b\]undle azonosító alapján (lásd a `osascript` oldalon):

`open -b {{com.domain.application}}`

- Nyissa meg az aktuális könyvtárat a Finderben:

`open .`

- \[R\]eveal a file in Finder:

`open -R {{path/to/file}}`

- Az aktuális könyvtárban lévő összes adott kiterjesztésű fájl megnyitása a hozzátartozó alkalmazással:

`open {{*.ext}}`

- A \[b\]ésle azonosítóval megadott alkalmazás \[n\]ew példányának megnyitása:

`open -n -b {{com.domain.application}}`
