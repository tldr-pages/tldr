# musescore

> MuseScore 3 kottaszerkesztő. További információk: <https://musescore.org/en/handbook/3/command-line-options>.

- Használjon speciális audioillesztőprogramot:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Állítsa be az MP3 kimeneti bitrátát kbit/s-ban:

`musescore --bitrate {{bitrate}}`

- Indítsa el a MuseScore-t hibakeresési módban:

`musescore --debug`

- Engedélyezze a kísérleti funkciókat, például a rétegeket:

`musescore --experimental`

- Az adott fájl exportálása a megadott kimeneti fájlba. A fájltípus a megadott kiterjesztéstől függ:

`musescore --export-to {{output_file}} {{input_file}}`

- A megadott pontszámok közötti különbség kiírása:

`musescore --diff {{path/to/file1}} {{path/to/file2}}`

- Adjon meg egy MIDI-import műveletfájlt:

`musescore --midi-operations {{path/to/file}}`
