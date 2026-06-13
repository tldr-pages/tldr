# apt-file

> Suche nach Dateien in apt-Paketen, auch in den nicht-installierten.
> Weitere Informationen: <https://manned.org/apt-file>.

- Aktualisiere die Metadatenbank:

`sudo apt update`

- Suche nach Paketen, die die/den spezifizierten Pfad/Datei enthalten:

`apt-file {{[find|search]}} {{pfad/zu/datei}}`

- Liste die Inhalte eines bestimmten Pakets auf:

`apt-file list {{paketname}}`

- Suche nach Paketen auf die die `regex` zutrifft:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{regular_expression}}`
