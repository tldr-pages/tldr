# lame

> 将 WAV 编码为 MP3 文件。
> 更多信息：<https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.

- 使用 320 kbit/秒的恒定比特率 (CBR) 将音频文件编码为 MP3：

`lame -b 320 {{path/to/file}}.wav {{path/to/output}}.mp3`

- 使用 V0 预设将音频文件编码为 MP3：

`lame -V 0 {{path/to/file}}.wav {{path/to/output}}.mp3`

- 将音频文件编码为 AAC：

`lame {{path/to/file}}.wav {{path/to/output}}.aac`