# git bugreport

> 收集系统和用户的调试信息，生成文本文件以帮助报告 Git 中的问题。
> 更多信息：<https://git-scm.com/docs/git-bugreport>.

- 在当前目录创建新的问题报告文件：

`git bugreport`

- 在指定目录创建新的问题报告文件（如目录不存在则自动创建）：

`git bugreport {{[-o|--output-directory]}} {{path/to/directory}}`

- 使用指定格式的时间戳后缀创建问题报告文件（ `strftime` 格式）：

`git bugreport {{[-s|--suffix]}} {{%m%d%y}}`
