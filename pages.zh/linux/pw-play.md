# pw-play

> 通过 PipeWire 播放音频文件。
> `pw-cat --playback` 的简写形式。
> 另请参见：`play`。
> 更多信息：<https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>。

- 通过默认目标播放 WAV 音频文件：

`pw-play {{path/to/file.wav}}`

- 以不同的音量级别播放 WAV 音频文件：

`pw-play --volume={{0.1}} {{path/to/file.wav}}`