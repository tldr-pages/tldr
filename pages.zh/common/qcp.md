# qcp

> 使用默认文本编辑器复制文件以定义文件名。
> 更多信息：<https://www.nongnu.org/renameutils/>.

- 复制单个文件（在左侧打开源文件名，在右侧打开目标文件名的编辑器）：

`qcp {{source_file}}`

- 复制多个JPEG文件：

`qcp {{*.jpg}}`

- 复制文件，但在编辑器中交换源文件名和目标文件名的位置：

`qcp --option swap {{*.jpg}}`