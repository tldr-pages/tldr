# timidity

> 播放和转换 MIDI 文件。
> 更多信息：<https://timidity.sourceforge.net>。

- 播放 MIDI 文件：

`timidity {{path/to/file.mid}}`

- 循环播放 MIDI 文件：

`timidity --loop {{path/to/file.mid}}`

- 以特定调播放 MIDI 文件（0 = C 大调/A 小调，-1 = F 大调/D 小调，+1 = G 大调/E 小调等）：

`timidity --force-keysig={{-flats|+sharps}} {{path/to/file.mid}}`

- 将 MIDI 文件转换为 PCM（WAV）音频：

`timidity --output-mode={{w}} --output-file={{path/to/file.wav}} {{path/to/file.mid}}`

- 将 MIDI 文件转换为 FLAC 音频：

`timidity --output-mode={{F}} --output-file={{path/to/file.flac}} {{path/to/file.mid}}`
