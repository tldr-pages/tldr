# gpg2

> GNU Privacy Guard 2.
> Siehe `gpg` für GNU Privacy Guard 1.
> Weitere Informationen: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- Liste alle importierten Schlüssel auf:

`gpg2 --list-keys`

- Verschlüssle eine bestimme Datei für einen bestimmten Empfänger und schreibe den Output in eine neue `.gpg` Datei:

`gpg2 --encrypt --recipient {{hans@beispiel.de}} {{pfad/zu/datei.txt}}`

- Verschlüssle eine bestimmte Datei nur mit einem Passwort und schreibe den Output in eine neue `.gpg` Datei:

`gpg2 --symmetric {{pfad/zu/datei.txt}}`

- Verschlüssle eine bestimmte Datei und schreibe das Ergebnis auf STDOUT:

`gpg2 --decrypt {{pfad/zu/datei.txt.gpg}}`

- Importiere einen öffentlichen Schlüssel:

`gpg2 --import {{pfad/zu/öffentlichem_schlüssel.gpg}}`

- Exportiere den öffentlichen Schlüssel einer bestimmten Email-Adresse nach STDOUT:

`gpg2 --export --armor {{hans@beispiel.de}}`

- Exportiere den privaten Schlüssel einer bestimmten Email-Adresse nach STDOUT:

`gpg2 --export-secret-keys --armor {{hans@beispiel.de}}`
