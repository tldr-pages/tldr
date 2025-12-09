# pbpaste

> 将剪贴板的内容发送到标准输出。
> 相当于在键盘上按下 `<Cmd v>`.
> 更多信息：<https://keith.github.io/xcode-man-pages/pbcopy.1>.

- 将剪贴板的内容写入文件：

`pbpaste > {{路径/到/文件}}`

- 将剪贴板的内容用作命令的输入：

`pbpaste | grep foo`
