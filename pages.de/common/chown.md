# chown

> Ändere den Besitzer und die Besitzergruppe von Dateien und Verzeichnissen.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/chown>.

- Ändere den Besitzer einer Datei/eines Verzeichnisses:

`chown {{benutzer}} {{pfad/zu/datei_oder_verzeichnis}}`

- Ändere den Besitzer und die Besitzergruppe einer Datei/eines Verzeichnisses:

`chown {{benutzer}}:{{gruppe}} {{pfad/zu/datei_oder_verzeichnis}}`

- Ändere den Besitzer eines Verzeichnisses rekursiv:

`chown -R {{benutzer}} {{pfad/zu/verzeichnis}}`

- Ändere den Besitzer eines symbolischen Links:

`chown -h {{benutzer}} {{pfad/zu/symlink}}`

- Ändere den Besitzer einer Datei/eines Verzeichnisses, damit sie/es mit einer Referenzdatei übereinstimmt:

`chown --reference {{pfad/zu/referenzdatei_oder_verzeichnis}} {{pfad/zu/datei_oder_verzeichnis}}`
