# flite

> 语音合成引擎。
> 更多信息：<http://www.festvox.org/flite/doc/>。

- 列出所有可用的语音：

`flite -lv`

- 将文本字符串转换为语音：

`flite -t "{{string}}"`

- 将文件内容转换为语音：

`flite -f {{path/to/file.txt}}`

- 使用指定的语音：

`flite -voice {{file://path/to/filename.flitevox|url}}`

- 将输出存储为 wav 文件：

`flite -voice {{file://path/to/filename.flitevox|url}} -f {{path/to/file.txt}} -o {{output.wav}}`

- 显示版本：

`flite --version`