# shnsplit

> 根据 `.cue` 文件分割音频文件。
> 更多信息：<http://shnutils.freeshell.org/shntool/>。

- 将 `.wav` 和 `.cue` 文件分割成多个文件：

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}}`

- 显示支持的格式：

`shnsplit -a`

- 将 `.flac` 文件分割成多个文件：

`shnsplit -f {{path/to/file.cue}} -o flac {{path/to/file.flac}}`

- 将 `.wav` 文件分割成 "track-number - album - title" 格式的文件：

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}} -t "%n - %a - %t"`