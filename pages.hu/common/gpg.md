# gpg

> GNU Privacy Guard. Lásd `gpg2` a GNU Privacy Guard 2-t. A legtöbb operációs rendszer a `gpg` szimbolikus linket a `gpg2` címre helyezi. További információ: <https://gnupg.org>.

- GPG nyilvános és privát kulcs létrehozása interaktív módon:

`gpg --full-generate-key`

- Aláírja a `doc.txt` titkosítás nélkül (a kimenetet a `doc.txt.asc` címre írja):

`gpg --clearsign {{doc.txt}}`

- A `doc.txt` titkosítása és aláírása a alice@example.com és a bob@example.com számára (kimenet a `doc.txt.gpg`):

`gpg --encrypt --sign --recipient {{alice@example.com}} --recipient {{bob@example.com}} {{doc.txt}}`

- A `doc.txt` titkosítása csak egy jelszóval (kimenet a `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- A `doc.txt.gpg` titkosításának visszafejtése (kimenet: `stdout`):

`gpg --decrypt {{doc.txt.gpg}}`

- Nyilvános kulcs importálása:

`gpg --import {{public.gpg}}`

- A alice@example.com nyilvános kulcsának exportálása (kimenet a `stdout`):

`gpg --export --armor {{alice@example.com}}`

- Privát kulcs exportálása a alice@example.com (kimenet: `stdout`):

`gpg --export-secret-keys --armor {{alice@example.com}}`
