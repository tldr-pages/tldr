# qcp

> 使用默认文本编辑器复制文件，以定义文件名。
> 更多信息：<https://www.nongnu.org/renameutils/>.

- 复制单个文件（在编辑器中打开左侧为源文件名，右侧为目标文件名的界面）：

`qcp {{源文件}}`

- 复制多个 JPEG 文件：

`qcp {{*.jpg}}`

- 复制文件，但在编辑器中交换源文件名和目标文件名的位置：

`qcp --option swap {{*.jpg}}`
