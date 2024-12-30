# cloc

> 统计源代码和注释的行数，并计算差异。
> 更多信息：<https://github.com/AlDanial/cloc>。

- 统计目录中的所有代码行数：

`cloc {{path/to/directory}}`

- 统计目录中的所有代码行数，在计数过程中显示进度条：

`cloc --progress=1 {{path/to/directory}}`

- 比较两个目录结构并计算它们之间的差异：

`cloc --diff {{path/to/directory/one}} {{path/to/directory/two}}`

- 忽略被版本控制系统（VCS）忽略的文件，例如在 `.gitignore` 中指定的文件：

`cloc --vcs git {{path/to/directory}}`

- 统计目录中的所有代码行数，显示每个文件的结果而不是每种语言的结果：

`cloc --by-file {{path/to/directory}}`