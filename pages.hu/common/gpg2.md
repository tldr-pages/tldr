# gpg2

> GNU Privacy Guard 2. Lásd `gpg` a GNU Privacy Guard 1. További információ: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- Importált kulcsok listája:

`gpg2 --list-keys`

- Egy megadott fájl titkosítása egy megadott címzett számára, a kimenetet egy új fájlba írja a `.gpg` címmel:

`gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}`

- Egy megadott fájl titkosítása csak egy jelszóval, a kimenetet egy új fájlba írja a `.gpg` függelékkel:

`gpg2 --symmetric {{path/to/doc.txt}}`

- Megadott fájl visszafejtése, az eredményt a standard kimenetre írja:

`gpg2 --decrypt {{path/to/doc.txt.gpg}}`

- Nyilvános kulcs importálása:

`gpg2 --import {{path/to/public_key.gpg}}`

- Egy megadott e-mail cím nyilvános kulcsának exportálása a standard kimenetre:

`gpg2 --export --armor {{alice@example.com}}`

- Egy megadott e-mail cím privát kulcsának exportálása a standard kimenetre:

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
