# MIXER

> Display/set sound levels.
> More information: <https://www.dosbox.com/wiki/MIXER>.

- Display current volumes:

`MIXER`

- Set master volume (left:right percentages):

`MIXER master {{80}}:{{80}}`

- Set Sound Blaster volume in decibels:

`MIXER sb d{{10}}:d{{10}}`

- Set GUS left channel only:

`MIXER gus {{50}}`

- Set volumes without displaying result:

`MIXER gus {{40}}:{{40}} /NOSHOW`

- List available MIDI devices (Windows only):

`MIXER /LISTMIDI`
