# cipher

> Zeigt oder Verändert die Verschlüsselung von Verzeichnissen und Dateien auf NTFS-Laufwerken.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Informationen über die Verschlüsselung einer bestimmten Datei oder eines Verzeichnisses anzeigen lassen:

`cipher /c:{{pfad/zu/datei_oder_verzeichnis}}`

- Verschlüssle eine Datei oder ein Verzeichnis (nachträglich hinzugefügte Dateien werden ebenfalls verschlüsselt, da das Verzeichnis markiert ist):

`cipher /e:{{pfad/zu/datei_oder_verzeichnis}}`

- Entschlüssle eine Datei oder ein Verzeichnis:

`cipher /d:{{pfad/zu/datei_oder_verzeichnis}}`

- Entferne eine Datei oder ein Verzeichnis sicher:

`cipher /w:{{pfad/zu/datei_oder_verzeichnis}}`
