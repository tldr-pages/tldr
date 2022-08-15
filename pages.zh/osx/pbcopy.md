# pbcopy

> 将标准输出放入剪贴板（命令行里的 cmd + C）。
> 更多信息：<https://ss64.com/osx/pbcopy.html>.

- 将文件的内容放入剪贴板：

`pbcopy < {{文件}}`

- 将命令的执行结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`
