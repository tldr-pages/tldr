# qcp

> 使用默认的文本编辑器复制文件以定义文件名。
> 更多信息：<https://www.nongnu.org/renameutils/>.

- 复制单个文件（打开一个编辑器，左侧是源文件名，右侧是目标文件名）：

`qcp {{source_file}}`

- 复制多个 JPEG 文件：

`qcp {{*.jpg}}`

- 复制文件，但在编辑器中交换源文件名和目标文件名的位置：

`qcp --option swap {{*.jpg}}`
