# qmv

> 使用默认文本编辑器定义文件名来移动文件和目录。
> 更多信息：<https://www.nongnu.org/renameutils/>。

- 移动单个文件（在左侧打开源文件名，在右侧打开目标文件名的编辑器）：

`qmv {{source_file}}`

- 移动多个JPEG文件：

`qmv {{*.jpg}}`

- 移动多个目录：

`qmv -d {{path/to/directory1}} {{path/to/directory2}} {{path/to/directory3}}`

- 移动目录中的所有文件和目录：

`qmv --recursive {{path/to/directory}}`

- 移动文件，但在编辑器中交换源文件名和目标文件名的位置：

`qmv --option swap {{*.jpg}}`

- 重命名当前目录中的所有文件和文件夹，但在编辑器中仅显示目标文件名（可以将其视为一种简单模式）：

`qmv --format=do .`