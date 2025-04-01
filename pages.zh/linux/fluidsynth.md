# fluidsynth

> 从 MIDI 文件合成音频。
> 更多信息：<https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- 播放 MIDI 文件：

`fluidsynth {{path/to/soundfont.sf2}} {{path/to/file.midi}}`

- 指定音频驱动：

`fluidsynth {{[-a|--audio-driver]}} {{pipewire|pulseaudio}} {{path/to/soundfont.sf2}} {{path/to/file.midi}}`

- 显示帮助：

`fluidsynth {{[-h|--help]}}`