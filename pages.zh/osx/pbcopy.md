# pbcopy

> 将数据从 `stdin` 复制到剪贴板。
> 相当于按下键盘上的 Cmd + C。
> 更多信息：<https://keith.github.io/xcode-man-pages/pbcopy.1.html>。

- 将特定文件的内容放入剪贴板：

`pbcopy < {{path/to/file}}`

- 将特定命令的结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`