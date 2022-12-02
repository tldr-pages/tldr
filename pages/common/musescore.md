# musescore

> MuseScore 3 sheet music editor.
> More information: <https://musescore.org/en/handbook/3/command-line-options>.

- Use a specific audio driver:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Set the MP3 output bitrate in kbit/s:

`musescore --bitrate {{bitrate}}`

- Start MuseScore in debug mode:

`musescore --debug`

- Enable experimental features, such as layers:

`musescore --experimental`

- Export the given file to the specified output file. The file type depends on the given extension:

`musescore --export-to {{path/to/file}} {{path/to/file}}`

- Print a diff between the given scores:

`musescore --diff {{path/to/file1 path/to/file2 ...}}`

- Specify a MIDI import operations file:

`musescore --midi-operations {{path/to/file}}`
