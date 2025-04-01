# pw-cat

> 通过 PipeWire 播放和录制音频文件。
> 更多信息：<https://docs.pipewire.org/page_man_pw-cat_1.html>。

- 通过默认目标播放 WAV 文件：

`pw-cat --playback {{path/to/file.wav}}`

- 使用指定的重采样质量（默认为 4）播放 WAV 文件：

`pw-cat --quality {{0..15}} --playback {{path/to/file.wav}}`

- 以 125% 的音量录制示例录音：

`pw-cat --record --volume {{1.25}} {{path/to/file.wav}}`

- 使用不同的采样率录制示例录音：

`pw-cat --record --rate {{6000}} {{path/to/file.wav}}`

- 显示帮助：

`pw-cat {{[-h|--help]}}`