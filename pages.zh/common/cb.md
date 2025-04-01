# cb

> 在终端中剪切、复制和粘贴任何内容。
> 更多信息：<https://github.com/Slackadays/Clipboard>.

- 显示所有剪贴板内容：

`cb`

- 将文件复制到剪贴板：

`cb copy {{path/to/file}}`

- 将一些文本复制到剪贴板：

`cb copy "{{Some example text}}"`

- 将管道数据复制到剪贴板：

`echo "{{Some example text}}" | cb`

- 粘贴剪贴板内容：

`cb paste`

- 输出剪贴板内容：

`cb | cat`

- 显示剪贴板历史记录：

`cb history`

- 显示剪贴板信息：

`cb info`
