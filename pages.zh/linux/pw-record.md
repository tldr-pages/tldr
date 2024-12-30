# pw-record

> 通过 PipeWire 录制音频文件。
> pw-cat --record 的简写。
> 更多信息：<https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>。

- 使用默认目标录制一个示例录音：

`pw-record {{path/to/file.wav}}`

- 以不同音量级别录制一个示例录音：

`pw-record --volume={{0.1}} {{path/to/file.wav}}`

- 使用不同采样率录制一个示例录音：

`pw-record --rate={{6000}} {{path/to/file.wav}}`