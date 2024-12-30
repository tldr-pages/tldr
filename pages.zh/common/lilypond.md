# lilypond

> 排版音乐和/或从文件生成MIDI。
> 另请参阅：`musescore`。
> 更多信息：<https://lilypond.org>。

- 将lilypond文件编译成PDF：

`lilypond {{path/to/file}}`

- 编译为指定格式：

`lilypond --formats={{format_dump}} {{path/to/file}}`

- 编译指定文件，抑制进度更新：

`lilypond -s {{path/to/file}}`

- 编译指定文件，并指定输出文件名：

`lilypond --output={{path/to/output_file}} {{path/to/input_file}}`

- 显示当前lilypond版本：

`lilypond --version`