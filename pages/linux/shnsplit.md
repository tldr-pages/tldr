# shnsplit

> Splits audio files according to a `.cue` file.
> More information: <http://shnutils.freeshell.org/shntool/>.

- Split a `.wav` + `.cue` file into multiple files:

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}}`

- Show supported formats:

`shnsplit -a`

- Split a `.flac` file into multiple files:

`shnsplit -f {{path/to/file.cue}} -o flac {{path/to/file.flac}}`

- Split a `.wav` file into files of the form "track-number - album - title":

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}} -t "%n - %a - %t`
