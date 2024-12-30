# espeak

> 使用文本转语音通过默认声音设备进行发声。
> 更多信息：<https://espeak.sourceforge.net>。

- 大声朗读一句话：

`espeak "我喜欢骑自行车。"`

- 大声朗读一个文件：

`espeak -f {{path/to/file}}`

- 将输出保存为WAV音频文件，而不是直接发声：

`espeak -w {{filename.wav}} "这是GNU加Linux"`

- 使用不同的语音：

`espeak -v {{voice}}`