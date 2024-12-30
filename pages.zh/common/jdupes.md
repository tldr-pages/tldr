# jdupes

> 一个强大的重复文件查找工具，是 fdupes 的增强版。
> 更多信息：<https://codeberg.org/jbruchon/jdupes>。

- 搜索单个目录：

`jdupes {{path/to/directory}}`

- 搜索多个目录：

`jdupes {{directory1}} {{directory2}}`

- 递归搜索所有目录：

`jdupes --recurse {{path/to/directory}}`

- 递归搜索目录并让用户选择要保留的文件：

`jdupes --delete --recurse {{path/to/directory}}`

- 搜索多个目录，并在 directory2 下跟随子目录，而不是 directory1：

`jdupes {{directory1}} --recurse: {{directory2}}`

- 搜索多个目录，并保持结果中的目录顺序：

`jdupes -O {{directory1}} {{directory2}} {{directory3}}`