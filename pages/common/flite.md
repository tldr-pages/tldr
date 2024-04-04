# flite

> Speech synthesis engine.
> More information: <http://www.festvox.org/flite/doc/>.

- List all available voices:

`flite -lv`

- Convert a text string to speech:

`flite -t "{{string}}"`

- Convert the contents of a file to speech:

`flite -f {{path/to/file.txt}}`

- Use the specified voice:

`flite -voice {{file://path/to/filename.flitevox|url}}`

- Store output into a wav file:

`flite -voice {{file://path/to/filename.flitevox|url}} -f {{path/to/file.txt}} -o {{output.wav}}`

- Display version:

`flite --version`
