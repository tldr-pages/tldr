# musescore

> MuseScore 3 乐谱编辑器。
> 另见：`lilypond`。
> 更多信息：<https://musescore.org/en/handbook/3/command-line-options>。

- 使用特定的音频驱动程序：

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- 设置 MP3 输出比特率（以 kbit/s 为单位）：

`musescore --bitrate {{bitrate}}`

- 以调试模式启动 MuseScore：

`musescore --debug`

- 启用实验性功能，例如图层：

`musescore --experimental`

- 将给定文件导出到指定的输出文件。文件类型取决于给定的扩展名：

`musescore --export-to {{output_file}} {{input_file}}`

- 打印给定乐谱之间的差异：

`musescore --diff {{path/to/file1}} {{path/to/file2}}`

- 指定 MIDI 导入操作文件：

`musescore --midi-operations {{path/to/file}}`