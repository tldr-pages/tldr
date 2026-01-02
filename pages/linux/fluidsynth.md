# fluidsynth

> Synthesize audio from MIDI files.
> More information: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- Play a MIDI file:

`fluidsynth {{/usr/share/soundfonts/soundfont.sf2}} {{path/to/file.midi}}`

- Specify the audio driver:

`fluidsynth {{[-a|--audio-driver]}} {{pipewire|pulseaudio}} {{/usr/share/soundfonts/soundfont.sf2}} {{path/to/file.midi}}`

- Display help:

`fluidsynth {{[-h|--help]}}`
