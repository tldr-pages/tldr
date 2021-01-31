# gpg

> GNU Privacy Guard.
> Mehr Informationen: <https://gnupg.org>.

- Signiere `doc.txt` ohne Verschlüsselung (Ausabe nach `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Verschlüssle `doc.txt` für alice@beispiel.de (Ausgabe nach `doc.txt.gpg`):

`gpg --encrypt --recipient {{alice@beispiel.de}} {{doc.txt}}`

- Verschlüssle `doc.txt` nur mit Passwort (Ausgabe nach `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- Entschlüssle `doc.txt.gpg` (Ausgabe nach stdout):

`gpg --decrypt {{doc.txt.gpg}}`

- Importiere einen Öffentlichen Schlüssel:

`gpg --import {{public.gpg}}`

- Exportiere Öffentlichen Schlüssel von alice@beispiel.de (Ausgabe nach stdout):

`gpg --export --armor {{alice@beispiel.de}}`

- Exportiere Privaten Schlüssel von alice@beispiel.de (Ausgabe nach stdout):

`gpg --export-secret-keys --armor {{alice@beispiel.de}}`
