# git bugreport

> 捕获系统和用户的调试信息，生成一个文本文件，以帮助报告 Git 中的错误。
> 更多信息：<https://git-scm.com/docs/git-bugreport>。

- 在当前目录中创建一个新的错误报告文件：

`git bugreport`

- 在指定目录中创建一个新的错误报告文件，如果该目录不存在则创建它：

`git bugreport {{-o|--output-directory}} {{path/to/directory}}`

- 使用指定的 `strftime` 格式的文件名后缀创建一个新的错误报告文件：

`git bugreport {{-s|--suffix}} {{%m%d%y}}`