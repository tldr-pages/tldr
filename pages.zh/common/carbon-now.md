# carbon-now

> 创建美丽的代码图像。
> 更多信息：<https://github.com/mixn/carbon-now-cli>。

- 使用默认设置从文件创建图像：

`carbon-now {{path/to/file}}`

- 使用默认设置从剪贴板中的文本创建图像：

`carbon-now --from-clipboard`

- 使用默认设置从 `stdin` 创建图像并复制到剪贴板：

`{{input}} | carbon-now --to-clipboard`

- 以交互方式创建图像以进行自定义设置，并可选择保存预设：

`carbon-now -i {{path/to/file}}`

- 从先前保存的预设创建图像：

`carbon-now -p {{preset}} {{path/to/file}}`

- 从指定文本行[s]tart：

`carbon-now -s {{line}} {{path/to/file}}`

- 在特定文本行[e]nd：

`carbon-now -e {{line}} {{path/to/file}}`

- 在浏览器中打开图像而不是保存：

`carbon-now --open {{path/to/file}}`