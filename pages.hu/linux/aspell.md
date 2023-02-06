# aspell

> Interaktív helyesírás-ellenőrző. További információ: <http://aspell.net/>.

- Egyetlen fájl helyesírás-ellenőrzése:

`aspell check {{path/to/file}}`

- A hibásan írt szavak listázása a standard bemenetről:

`cat {{path/to/file}} | aspell list`

- A rendelkezésre álló szótári nyelvek megjelenítése:

`aspell dicts`

- A `aspell` futtatása más nyelvvel (kétbetűs ISO 639 nyelvi kódot vesz fel):

`aspell --lang={{cs}}`

- Rosszul írt szavak listázása a standard bemenetről és a személyes szólistán szereplő szavak figyelmen kívül hagyása:

`cat {{path/to/file}} | aspell --personal={{personal-word-list.pws}} list`
