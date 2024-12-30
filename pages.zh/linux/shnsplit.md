# shnsplit

> 根据 `.cue` 文件拆分音频文件。
> 更多信息：<http://shnutils.freeshell.org/shntool/>.

- 将 `.wav` + `.cue` 文件拆分为多个文件：

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}}`

- 显示支持的格式：

`shnsplit -a`

- 将 `.flac` 文件拆分为多个文件：

`shnsplit -f {{path/to/file.cue}} -o flac {{path/to/file.flac}}`

- 将 `.wav` 文件拆分为 "track-number - album - title" 形式的文件：

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}} -t "%n - %a - %t"`