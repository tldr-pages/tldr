# cdparanoia

> Extrahiere Titel von Audio-CDs.
> Weitere Informationen: <https://xiph.org/paranoia/index.html>.

- Extrahiere alle Titel und schreibe sie in separate WAV-Dateien mit dem Namen `track#.wav`:

`cdparanoia {{[-B|--batch]}}`

- Gib das Inhaltsverzeichnis der CD auf der Konsole aus:

`cdparanoia {{[-Q|--query]}}`

- Extrahiere Titel 2 bis 5 und schreibe sie zusammen in eine WAV-Datei:

`cdparanoia 2-5`

- Extrahiere Titel 3 und schreibe ihn in eine Datei mit dem Namen `pfad/zu/datei.wav`:

`cdparanoia 3 '{{pfad/zu/datei.wav}}'`
