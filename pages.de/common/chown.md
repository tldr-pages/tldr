# chown

> Ändere den Besitzer und die Besitzergruppe von Dateien und Verzeichnissen.

- Ändere den Besitzer einer Datei/eines Verzeichnisses:

`chown {{benutzer}} {{pfad/zu/datei_oder_verzeichnis}}`

- Ändere den Besitzer und die Besitzergruppe einer Datei/eines Verzeichnisses:

`chown {{benutzer}}:{{gruppe}} {{pfad/zu/datei_oder_verzeichnis}}`

- Ändere den Besitzer eines Verzeichnisses und seines Inhalts rekursiv:

`chown -R {{benutzer}} {{pfad/zu/Verzeichnis}}`

- Ändere den Besitzer eines symbolischen Links:

`chown -h {{benutzer}} {{pfed/zu/symlink}}`

- Ändere den Besitzer einer Datei/eines Verzeichnisses, damit sie/es mit einer Referenzdatei übereinstimmt:

`chown --reference={{pfad/zu/referenzdatei}} {{pfad/zu/datei_oder_verzeichnis}}`
