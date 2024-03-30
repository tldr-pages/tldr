# gpg

> GNU Privacy Guard.
> Siehe `gpg2` für GNU Privacy Guard 2.
> Weitere Informationen: <https://gnupg.org>.

- Erstelle einen öffentlichen und privaten GPG Schlüssel interaktiv:

`gpg --full-generate-key`

- Signiere `doc.txt` ohne Verschlüsselung (Ausgabe nach `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Verschlüssle und signiere `doc.txt` für alice@beispiel.de und bob@example.org (Ausgabe nach `doc.txt.gpg`):

`gpg --encrypt --sign --recipient {{alice@beispiel.de}} --recipient {{bob@example.com}} {{doc.txt}}`

- Verschlüssle `doc.txt` nur mit Passwort (Ausgabe nach `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- Entschlüssle `doc.txt.gpg` (Ausgabe nach `stdout`):

`gpg --decrypt {{doc.txt.gpg}}`

- Importiere einen öffentlichen Schlüssel:

`gpg --import {{schlüssel.gpg}}`

- Exportiere den öffentlichen Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export --armor {{alice@beispiel.de}}`

- Exportiere den privaten Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export-secret-keys --armor {{alice@beispiel.de}}`
