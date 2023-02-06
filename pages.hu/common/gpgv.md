# gpgv

> OpenPGP aláírások ellenőrzése. További információ: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- Aláírt fájl ellenőrzése:

`gpgv {{path/to/file}}`

- Aláírt fájl ellenőrzése leválasztott aláírással:

`gpgv {{path/to/signature}} {{path/to/file}}`

- Fájl hozzáadása a kulcskarikák listájához (egy exportált kulcs is kulcskarikának számít):

`gpgv --keyring {{./alice.keyring}} {{path/to/signature}} {{path/to/file}}`
