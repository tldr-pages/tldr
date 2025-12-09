# jp2a

> 将 JPEG 图像转换为 ASCII。
> 更多信息：<https://manned.org/jp2a>.

- 从文件中读取 JPEG 图像并以 ASCII 显示：

`jp2a {{路径/到/image.jpeg}}`

- 从 URL 中读取 JPEG 图像并以 ASCII 显示：

`jp2a {{www.example.com/image.jpeg}}`

- 对 ASCII 输出进行着色：

`jp2a --colors {{路径/到/image.jpeg}}`

- 指定用于 ASCII 输出的字符：

`jp2a --chars='{{..-ooxx@@}}' {{路径/到/image.jpeg}}`

- 将 ASCII 输出写入一个文件：

`jp2a --output={{路径/到/output_file.txt}} {{路径/到/image.jpeg}}`

- 以 HTML 文件格式写入 ASCII 输出，适合在网页浏览器中查看：

`jp2a --html --output={{路径/到/output_file.html}} {{路径/到/image.jpeg}}`
