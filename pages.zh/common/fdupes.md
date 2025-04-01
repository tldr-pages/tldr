# fdupes

> 在一组目录中查找重复文件。
> 更多信息：<https://github.com/adrianlopezroche/fdupes>。

- 搜索单个目录：

`fdupes {{path/to/directory}}`

- 搜索多个目录：

`fdupes {{directory1}} {{directory2}}`

- 递归搜索目录：

`fdupes -r {{path/to/directory}}`

- 搜索多个目录，其中一个递归：

`fdupes {{directory1}} -R {{directory2}}`

- 递归搜索，将硬链接视为重复文件：

`fdupes -rH {{path/to/directory}}`

- 递归搜索重复文件并显示交互式提示选择要保留的文件，删除其他文件：

`fdupes -rd {{path/to/directory}}`

- 递归搜索并删除重复文件，不提示确认：

`fdupes -rdN {{path/to/directory}}`
