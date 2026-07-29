# cloc

> 统计代码行数。
> 更多信息：<https://github.com/AlDanial/cloc#options->。

- 统计目录中所有代码的行数：

`cloc {{路径/到/目录}}`

- 比较两个目录结构并统计它们之间的差异：

`cloc --diff {{路径/到/目录1}} {{路径/到/目录2}}`

- 忽略版本控制系统忽略的文件（如 `.gitignore` 中指定的文件）：

`cloc --vcs git {{路径/到/目录}}`

- 按文件显示结果，而不是按语言汇总：

`cloc --by-file {{路径/到/目录}}`
