# shnsplit

> Splits audio files according to a .cue file.
> More information: <http://shnutils.freeshell.org/shntool/>.

- Split a wav + cue file into multiple files:

`shnsplit -f file.cue file.wav`

- Show supported formats

`shnsplit -a`

- Splits a flac file into multiple files

`shnsplit -f file.cue -o flac file.flac`

- Splits a wav file into files of the form track-number - album - title:

`shnsplit -f file.cue file.wav -t "%n - %a - %t`
