# asciiart

> 将图像转换为ASCII。
> 更多信息：<https://github.com/nodanaonlyzuul/asciiart>。

- 从文件中读取图像并以ASCII格式打印：

`asciiart {{path/to/image.jpg}}`

- 从URL中读取图像并以ASCII格式打印：

`asciiart {{www.example.com/image.jpg}}`

- 选择输出宽度（默认是100）：

`asciiart --width {{50}} {{path/to/image.jpg}}`

- 为ASCII输出上色：

`asciiart --color {{path/to/image.jpg}}`

- 选择输出格式（默认格式是文本）：

`asciiart --format {{text|html}} {{path/to/image.jpg}}`

- 反转字符映射：

`asciiart --invert-chars {{path/to/image.jpg}}`