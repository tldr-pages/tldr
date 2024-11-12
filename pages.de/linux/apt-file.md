# apt-file

> Suche nach Dateien in apt-Paketen, auch in den nicht-installierten.
> Weitere Informationen: <https://manned.org/apt-file.1>.

- Aktualisiere die Metadatenbank:

`sudo apt update`

- Suche nach Paketen, die die/den spezifizierten Pfad/Datei enthalten:

`apt-file {{search|find}} {{pfad/zu/datei}}`

- Liste die Inhalte eines bestimmten Pakets auf:

`apt-file {{show|list}} {{paketname}}`

- Suche nach Paketen auf die die Regular Expression zutrifft:

`apt-file {{search|find}} --regexp {{regular_expression}}`
