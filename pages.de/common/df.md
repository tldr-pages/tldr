# df

> Verschafft einen Überblick über verfügbaren Speicherplatz im Dateisystem.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/df>.

- Zeige verfügbaren Platz auf allen eingehängten Dateisystemen:

`df`

- Zeige verfügbaren Platz auf allen eingehängten Dateisystemen in einem menschenlesbaren Format:

`df -h`

- Zeige das Dateisystem und dessen Speicherverbrauch, das die angegebene Datei oder Verzeichnis enthält:

`df {{pfad/zu/datei_oder_verzeichnis}}`

- Zeige Statistiken über die Anzahl freier Inodes:

`df -i`

- Zeige alle Dateisysteme bis auf die eines bestimmten Typs:

`df -x {{squashfs}} -x {{tmpfs}}`
