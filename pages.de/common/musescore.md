# musescore

> MuseScore 3 Notenblatt-Editor.
> Weitere Informationen: <https://musescore.org/en/handbook/3/command-line-options>.

- Verwende einen bestimmten Audio-Treiber:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Setze die MP3 Output-Bitrate in kbit/s:

`musescore --bitrate {{bitrate}}`

- Starte MuseScore im Debug-Modus:

`musescore --debug`

- Aktiviere experimentelle Funktionen, wie Layer:

`musescore --experimental`

- Exportiere eine Datei in ein anderes Format. Dieses hängt von der Dateierweiterung ab:

`musescore --export-to {{output_datei}} {{input_datei}}`

- Zeige Unterschiede zwischen zwei Partituren:

`musescore --diff {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Gib eine MIDI-Importoperationsdatei an:

`musescore --midi-operations {{pfad/zu/datei}}`
