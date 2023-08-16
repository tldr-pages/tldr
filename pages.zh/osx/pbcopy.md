# pbcopy

> 将来自标准输入的数据放入剪贴板。
> 相当于在键盘上按下 Cmd + C.
> 更多信息：<https://ss64.com/osx/pbcopy.html>.

- 将文件的内容放入剪贴板：

`pbcopy < {{路径/到/文件}}`

- 将命令的执行结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`
