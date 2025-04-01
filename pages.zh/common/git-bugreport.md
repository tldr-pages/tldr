# git bugreport

> 从系统和用户捕获调试信息，生成一个文本文件，以帮助报告 Git 中的错误。
> 更多信息：<https://git-scm.com/docs/git-bugreport>.

- 在当前目录中创建一个新的错误报告文件：

`git bugreport`

- 在指定目录中创建一个新的错误报告文件，如果目录不存在则创建它：

`git bugreport {{[-o|--output-directory]}} {{path/to/directory}}`

- 使用指定的 `strftime` 格式后缀创建一个新的错误报告文件：

`git bugreport {{[-s|--suffix]}} {{%m%d%y}}`