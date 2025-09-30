# gpg

> GNU Privacy Guard.
> Weitere Informationen: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- Erstelle einen öffentlichen und privaten GPG Schlüssel interaktiv:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- Signiere `doc.txt` ohne Verschlüsselung (Ausgabe nach `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Verschlüssle und signiere `doc.txt` für alice@beispiel.de und bob@example.org (Ausgabe nach `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@beispiel.de}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- Verschlüssle `doc.txt` nur mit Passwort (Ausgabe nach `doc.txt.gpg`):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- Entschlüssle `doc.txt.gpg` (Ausgabe nach `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Importiere einen öffentlichen Schlüssel:

`gpg --import {{schlüssel.gpg}}`

- Exportiere den öffentlichen Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export {{[-a|--armor]}} {{alice@beispiel.de}}`

- Exportiere den privaten Schlüssel von alice@beispiel.de (Ausgabe nach `stdout`):

`gpg --export-secret-keys {{[-a|--armor]}} {{alice@beispiel.de}}`
