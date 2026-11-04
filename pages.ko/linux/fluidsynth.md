# fluidsynth

> MIDI 파일로부터 오디오를 합성.
> 더 많은 정보: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- MIDI 파일 재생:

`fluidsynth {{/usr/share/soundfonts/soundfont.sf2}} {{경로/대상/파일.midi}}`

- 오디오 드라이버를 지정하여 MIDI 파일 재생:

`fluidsynth {{[-a|--audio-driver]}} {{pipewire|pulseaudio}} {{/usr/share/soundfonts/soundfont.sf2}} {{경로/대상/파일.midi}}`

- 도움말 표시:

`fluidsynth {{[-h|--help]}}`
