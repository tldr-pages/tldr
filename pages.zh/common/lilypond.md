# lilypond

> 从文件中排版音乐和/或生成 MIDI。
> 参见：`musescore`。
> 更多信息：<https://lilypond.org>。

- 将 lilypond 文件编译为 PDF：

`lilypond {{path/to/file}}`

- 将文件编译为指定的格式：

`lilypond --formats={{format_dump}} {{path/to/file}}`

- 编译指定的文件，抑制进度更新：

`lilypond -s {{path/to/file}}`

- 编译指定的文件，并指定输出文件名：

`lilypond --output={{path/to/output_file}} {{path/to/input_file}}`

- 显示当前 lilypond 的版本：

`lilypond --version`
