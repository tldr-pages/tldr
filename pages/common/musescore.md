# musescore

> MuseScore sheet music editor.
> See also: `lilypond`.
> More information: <https://handbook.musescore.org/appendix/command-line-usage>.

- Set the MP3 output bitrate in kbit/s:

`musescore {{[-b|--bitrate]}} {{bitrate}}`

- Start MuseScore in debug mode:

`musescore {{[-d|--debug]}}`

- Enable experimental features, such as layers:

`musescore {{[-e|--experimental]}}`

- Export the given file to the specified output file. The file type depends on the given extension:

`musescore {{[-o|--export-to]}} {{output_file}} {{input_file}}`

- Print a diff between the given scores:

`musescore --diff {{path/to/file1}} {{path/to/file2}}`

- Specify a MIDI import operations file:

`musescore {{[-M|--midi-operations]}} {{path/to/file}}`
