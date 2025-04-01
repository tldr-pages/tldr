# carbon-now

> 创建漂亮的代码图片。
> 更多信息：<https://github.com/mixn/carbon-now-cli>.

- 使用默认设置从文件创建图片：

`carbon-now {{文件}}`

- 使用默认设置从剪贴板创建图片：

`carbon-now --from-clipboard`

- 使用默认设置从标准输入创建图片：

`{{输入}} | carbon-now`

- 以交互方式创建图片以进行自定义设置，还可以选择保存预设：

`carbon-now -i {{文件}}`

- 从先前保存的预设创建图片：

`carbon-now -p {{预设}} {{文件}}`

- 从指定的文本行开始：

`carbon-now -s {{行号}} {{文件}}`

- 结束于指定的文本行：

`carbon-now -e {{行号}} {{文件}}`

- 在浏览器中打开图片而不是保存：

`carbon-now --open {{文件}}`
