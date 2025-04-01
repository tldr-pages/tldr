# tmsu

> 简单的命令行工具，用于给文件打标签。
> 更多信息：<https://tmsu.org>.

- 为特定文件添加多个标签：

`tmsu tag {{path/to/file.mp3}} {{music}} {{big-jazz}} {{mp3}}`

- 为多个文件添加标签：

`tmsu tag --tags "{{music mp3}}" {{*.mp3}}`

- 列出指定文件的标签：

`tmsu tags {{*.mp3}}`

- 列出带有指定标签的文件：

`tmsu files {{big-jazz}} {{music}}`

- 列出与布尔表达式匹配的标签文件：

`tmsu files "{{(year >= 1990 and year <= 2000)}} and {{grunge}}"`

- 将 tmsu 虚拟文件系统挂载到现有目录：

`tmsu mount {{path/to/directory}}`
