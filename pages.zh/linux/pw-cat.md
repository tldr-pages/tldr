# pw-cat

> 通过 PipeWire 播放和录制音频文件。
> 更多信息：<https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>。

- 通过默认目标播放 WAV 文件：

`pw-cat --playback {{path/to/file.wav}}`

- 以指定的重采样质量播放 WAV 文件（默认值为 4）：

`pw-cat --quality {{0..15}} --playback {{path/to/file.wav}}`

- 以 125% 的音量水平录制样本录音：

`pw-cat --record --volume {{1.25}} {{path/to/file.wav}}`

- 使用不同的采样率录制样本录音：

`pw-cat --record --rate {{6000}} {{path/to/file.wav}}`