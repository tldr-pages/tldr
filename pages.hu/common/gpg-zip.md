# gpg-zip

> Az archívumban lévő fájlok és könyvtárak titkosítása GPG használatával. További információ: <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- Egy könyvtár titkosítása a `archive.gpg` címre egy jelszóval:

`gpg-zip --symmetric --output {{archive.gpg}} {{path/to/directory}}`

- A `archive.gpg` visszafejtése egy azonos nevű könyvtárba:

`gpg-zip --decrypt {{path/to/archive.gpg}}`

- A titkosított `archive.gpg` tartalmának listázása:

`gpg-zip --list-archive {{path/to/archive.gpg}}`
