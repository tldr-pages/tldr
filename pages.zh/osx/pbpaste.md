# pbpaste

> 将剪贴板的内容发送到 `stdout`。
> 相当于在键盘上按下 Cmd + V。
> 更多信息：<https://keith.github.io/xcode-man-pages/pbpaste.1.html>。

- 将剪贴板的内容写入文件：

`pbpaste > {{path/to/file}}`

- 将剪贴板的内容作为命令的输入：

`pbpaste | grep foo`