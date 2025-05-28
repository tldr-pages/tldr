# gpg

> GNU Privacy Guard, een OpenPGP encryptie- en ondertekeningstool.
> Meer informatie: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- Maak interactief een GPG publieke en private sleutel:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- Geef alle sleutels van de publieke sleutelring weer:

`gpg {{[-k|--list-keys]}}`

- Onderteken `doc.txt` zonder encryptie (schrijft uitvoer naar `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Versleutel en onderteken `doc.txt` voor `alice@example.com` en `bob@example.com` (schrijft uitvoer naar `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--receiver]}} {{alice@example.com}} {{[-r|--receiver]}} {{bob@example.com}} {{doc.txt}}`

- Versleutel `doc.txt` met alleen een wachtwoordzin (uitvoer naar `doc.txt.gpg`):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- Ontcijfer `doc.txt.gpg` (uitvoer naar `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Importeer een publieke sleutel:

`gpg --import {{public.gpg}}`

- Exporteer de publieke/privé sleutel voor `alice@example.com` (uitvoer naar `stdout`):

`gpg {{--export|--export-secret-keys}} {{[-a|--armor]}} {{alice@example.com}}`
