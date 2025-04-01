# cot

> macOS 的纯文本编辑器。
> 更多信息：<https://coteditor.com/>.

- 启动 CotEditor:

`cot`

- 打开特定文件:

`cot {{path/to/file1 path/to/file2 ...}}`

- 打开一个新的空白文档:

`cot --new`

- 打开特定文件并阻塞终端，直到文件关闭:

`cot --wait {{path/to/file}}`

- 打开特定文件，并将光标定位在指定的行和列:

`cot --line {{1}} --column {{80}} {{path/to/file}}`
