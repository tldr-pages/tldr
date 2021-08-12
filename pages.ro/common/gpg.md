# gpg

> Garda de confidențialitate GNU.
> A se vedea `gpg2` pentru GNU Privacy Guard 2.
> Mai multe informaţii: <https://gnupg.org>

- Creați o cheie publică și privată GPG interactiv:

`gpg --full-generate-key`

- Semnează `doc.txt` fără criptare (scrie de ieșire la `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Criptare `doc.txt` pentru alice@example.com (ieșire la `doc.txt.gpg`):

`gpg --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- Criptează `doc.txt` numai cu o frază de acces (ieșire la `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- Decripta `doc.txt.gpg` (ieșire la stdout):

`gpg --decrypt {{doc.txt.gpg}}`

- Importați o cheie publică:

`gpg --import {{public.gpg}}`

- Export cheie publică pentru alice@example.com (ieșire la stdout):

`gpg --export --armor {{alice@example.com}}`

- Export cheie privată pentru alice@example.com (ieșire la stdout):

`gpg --export-secret-keys --armor {{alice@example.com}}`
