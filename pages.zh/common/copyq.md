# copyq

> 高级功能的剪贴板管理器。
> 更多信息：<https://copyq.readthedocs.io/en/latest/command-line.html>。

- 启动 CopyQ 以存储剪贴板历史记录：

`copyq`

- 显示当前剪贴板内容：

`copyq clipboard`

- 将纯文本插入剪贴板历史记录：

`copyq add -- {{text1}} {{text2}} {{text3}}`

- 将包含转义序列（'\n', '\t'）的文本插入剪贴板历史记录：

`copyq add {{firstline\nsecondline}}`

- 打印剪贴板历史记录中前 3 项的内容：

`copyq read 0 1 2`

- 将文件内容复制到剪贴板：

`copyq copy < {{path/to/file.txt}}`

- 将 JPEG 图像复制到剪贴板：

`copyq copy image/jpeg < {{path/to/image.jpg}}`