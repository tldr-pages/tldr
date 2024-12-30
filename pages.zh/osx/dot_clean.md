# dot_clean

> 合并 ._* 文件与相应的本地文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/dot_clean.1.html>。

- 递归合并所有 `._*` 文件：

`dot_clean {{path/to/directory}}`

- 不递归合并目录中的所有 `._*` 文件（扁平合并）：

`dot_clean -f {{path/to/directory}}`

- 合并并删除所有 `._*` 文件：

`dot_clean -m {{path/to/directory}}`

- 仅在存在匹配的本地文件时删除 `._*` 文件：

`dot_clean -n {{path/to/directory}}`

- 跟随符号链接：

`dot_clean -s {{path/to/directory}}`

- 打印详细输出：

`dot_clean -v {{path/to/directory}}`