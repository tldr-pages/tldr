# musescore

> MusesCore 3 editor de muzică foaie.
> Mai multe informaţii: <https://musescore.org/en/handbook/3/command-line-options>

- Utilizați un driver audio specific:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Setați bitrate de ieșire MP3 în kbit/s:

`musescore --bitrate {{bitrate}}`

- Porniți MusesCore în modul de depanare:

`musescore --debug`

- Activați caracteristicile experimentale, cum ar fi straturile:

`musescore --experimental`

- Exportați fișierul dat în fișierul de ieșire specificat. Tipul de fișier depinde de extensia dată:

`musescore --export-to {{output_file}} {{input_file}}`

- Imprimați o diferență între scorurile date:

`musescore --diff {{path/to/file1}} {{path/to/file2}}`

- Specificați un fișier de operațiuni de import MIDI:

`musescore --midi-operations {{path/to/file}}`
