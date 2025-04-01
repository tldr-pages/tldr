# moe

> 一个适用于 ISO-8859-15 编码文本的所见即所得文本编辑器。
> 更多信息：<https://www.gnu.org/software/moe/moe.html>.

- 打开 moe 并在保存编辑时创建备份文件（file~）：

`moe {{path/to/file}}`

- 以只读模式打开文件：

`moe {{[-o|--read-only]}} {{path/to/file}}`

- 编辑文件时不创建备份：

`moe {{[-B|--no-backup]}} {{path/to/file}}`

- 编辑文件时在搜索中忽略大小写：

`moe {{[-i|--ignore-case]}} {{path/to/file}}`

- 保存并退出：

`<Ctrl x>`
