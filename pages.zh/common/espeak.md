# espeak

> 使用文本转语音功能通过默认音频设备朗读文本。
> 更多信息：<https://espeak.sourceforge.net>.

- 朗读一段话：

`espeak "我喜欢骑自行车。"`

- 朗读文件内容：

`espeak -f {{path/to/file}}`

- 将输出保存为 WAV 音频文件，而不是直接朗读：

`espeak -w {{filename.wav}} "这是 GNU 加上 Linux"`

- 使用不同的声音：

`espeak -v {{voice}}`