# pass

> Jelszavak vagy más érzékeny adatok tárolására és olvasására szolgáló eszköz. Minden adat GPG-titkosítással van ellátva, és Git tárolóval kezelhető. További információ: <https://www.passwordstore.org>.

- A tároló inicializálása (vagy újbóli titkosítása) egy vagy több GPG azonosítóval:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Mentse el az új jelszót és a további információkat (a Ctrl + D billentyűkombinációval egy új sorban a befejezéshez):

`pass insert --multiline {{path/to/data}}`

- Egy bejegyzés szerkesztése:

`pass edit {{path/to/data}}`

- Jelszó másolása (az adatfájl első sora) a vágólapra:

`pass -c {{path/to/data}}`

- A teljes tárolófa listázása:

`pass`

- Új véletlenszerű jelszó generálása adott hosszúsággal, és másolása a vágólapra:

`pass generate -c {{path/to/data}} {{num}}`

- Egy új Git-tár inicializálása (a passzolással végrehajtott módosítások automatikusan le lesznek kötve):

`pass git init`

- Futtasson egy Git-parancsot a jelszótároló nevében:

`pass git {{command}}`
