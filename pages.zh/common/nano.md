# nano

> 命令行文本编辑器。增强版的 `Pico` 克隆。
> 更多信息：<https://nano-editor.org>。

- 启动编辑器：

`nano`

- 启动编辑器时不使用配置文件：

`nano --ignorercfiles`

- 打开特定文件，关闭上一个文件后自动移动到下一个文件：

`nano {{path/to/file1 path/to/file2 ...}}`

- 打开一个文件并将光标定位在特定行和列：

`nano +{{line}},{{column}} {{path/to/file}}`

- 打开一个文件并启用软换行：

`nano --softwrap {{path/to/file}}`

- 打开一个文件并将新行缩进到上一行的缩进位置：

`nano --autoindent {{path/to/file}}`

- 打开一个文件并在保存时创建备份文件（`path/to/file~`）：

`nano --backup {{path/to/file}}`