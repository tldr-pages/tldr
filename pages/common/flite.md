# flite

> Speech synthesis engine.
> More information: <http://www.festvox.org/flite/doc/>.

- Show flite version information:

`flite --version`

- List all available voices:

`flite -lv`

- Convert a text string to speech:

`flite -t "{{string}}"`

- Convert the contents of a file to speech:

`flite -f {{path/to/file}}`

- Specify which voice to use:

`flite -voice {{file://path/to/filename.flitevox | url}}`

- Store output into a wav file:

`flite -voice {{file://path/to/filename.flitevox | url}} -f {{path/to/textfile}} -o {{output.wav}}`
