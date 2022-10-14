# xcopy

> Kopieren von Dateien und Verzeichnisbäumen.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Kopieren der Datei(en) an den angegebenen Zielort:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}}`

- Auflisten der zu kopierenden Dateien vor dem Kopieren

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /p`

- Kopieren der Verzeichnisstruktur ohne Dateien:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /t`

- Leere Verzeichnisse beim Kopieren einbeziehen:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /e`

- Beibehalten der Quell-Zugriffsrichtlinien (ACL) im Ziel Verzeichniss:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /o`

- Wiederaufnahme des Vorgangs bei Unterbrechung der Netzwerkverbindung zulassen:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /z`

- Unterdrückt die Eingabeaufforderung, um zu bestätigen, dass Sie eine vorhandene Zieldatei überschreiben möchten:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zum/ziel}} /y`

- Zeigt die Hilfe an der Eingabeaufforderung an:

`xcopy /?`
