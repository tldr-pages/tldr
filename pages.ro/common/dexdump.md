# dexdump

> Afișați informații despre fișierele Android DEX.
> Mai multe informaţii: <https://manned.org/dexdump>

- Extragerea claselor și metodelor dintr-un fișier APK:

`dexdump {{path/to/file.apk}}`

- Afișează informații antet ale fișierelor DEX conținute într-un fișier APK:

`dexdump -f {{path/to/file.apk}}`

- Afișează ieșirea dezasamblată a secțiunilor executabile:

`dexdump -d {{path/to/file.apk}}`

- Rezultatele de ieșire într-un fișier:

`dexdump -o {{path/to/file}} {{path/to/file.apk}}`
