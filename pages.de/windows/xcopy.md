# xcopy

> Kopieren von Dateien und Verzeichnisbäumen.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Kopiere Datei(en) an den angegebenen Zielort:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}}`

- Liste die zu kopierenden Dateien vor dem Kopieren auf:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /p`

- Kopiere nur die Verzeichnisstruktur ohne Dateien:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /t`

- Kopiere leere Verzeichnisse mit:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /e`

- Behalte die Quell-Zugriffsrichtlinien (ACL) im Ziel Verzeichnis bei:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /o`

- Setze den Vorgang nach Unterbrechung der Netzwerkverbindung fort:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /z`

- Überschreibe bereits vorhandene Zieldateien automatisch:

`xcopy {{pfad/zu/datei_oder_verzeichnis}} {{pfad/zu/ziel}} /y`

- Zeige die detaillierte Hilfe an:

`xcopy /?`
