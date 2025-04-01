# cloc

> 统计源代码行数和注释行数，并计算差异。
> 更多信息：<https://github.com/AlDanial/cloc>。

- 统计目录中的所有代码行数：

`cloc {{path/to/directory}}`

- 统计目录中的所有代码行数，并在统计过程中显示进度条：

`cloc --progress=1 {{path/to/directory}}`

- 比较两个目录结构，并统计它们之间的差异：

`cloc --diff {{path/to/directory/one}} {{path/to/directory/two}}`

- 忽略版本控制系统（如 `.gitignore` 文件中指定的）忽略的文件：

`cloc --vcs git {{path/to/directory}}`

- 统计目录中的所有代码行数，并显示每个文件的结果，而不是每种语言的结果：

`cloc --by-file {{path/to/directory}}`