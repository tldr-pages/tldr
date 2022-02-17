# asciiart

> 将图像转换为 ASCII.
> 更多信息：<https://github.com/nodanaonlyzuul/asciiart>.

- 从文件中读取图像并以 ASCII 打印：

`asciiart {{路径/到/图片.jpg}}`

- 从 URL 中读取图像并以 ASCII 打印：

`asciiart {{www.example.com/image.jpg}}`

- 选择输出宽度（默认为 100）：

`asciiart -width {{50}} {{路径/到/图片.jpg}}`

- 对 ASCII 输出进行着色：

`asciiart --color {{路径/到/图片.jpg}}`

- 选择输出格式（默认格式为文本）：

`asciiart --format {{text|html}} {{路径/到/图片.jpg}}`

- 反转字符映射：

`asciiart --invert-chars {{路径/到/图片.jpg}}`
