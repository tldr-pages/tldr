# dconf

> A dconf adatbázisok kezelése. Lásd még: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`. További információ: <https://manned.org/dconf>.

- Egy adott kulcsérték kiírása:

`dconf read {{/path/to/key}}`

- Egy adott elérési útvonal alkönyvtárak és alkulcsok kiírása:

`dconf list {{/path/to/directory/}}`

- Egy adott kulcsérték kiírása:

`dconf write {{/path/to/key}} "{{value}}"`

- Egy adott kulcsérték visszaállítása:

`dconf reset {{/path/to/key}}`

- Egy adott kulcs/könyvtár változásainak figyelése:

`dconf watch {{/path/to/key|/path/to/directory/}}`

- Egy adott könyvtár kiürítése INI fájl formátumban:

`dconf dump {{/path/to/directory/}}`
