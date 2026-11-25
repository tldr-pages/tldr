# fluidsynth

> تولید صدا از فایل‌های MIDI.
> اطلاعات بیشتر: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- پخش یک فایل MIDI:

`fluidsynth {{/usr/share/soundfonts/soundfont.sf2}} {{path/to/file.midi}}`

- تعیین درایور صدا:

`fluidsynth {{[-a|--audio-driver]}} {{pipewire|pulseaudio}} {{/usr/share/soundfonts/soundfont.sf2}} {{path/to/file.midi}}`

- نمایش راهنما:

`fluidsynth {{[-h|--help]}}`
