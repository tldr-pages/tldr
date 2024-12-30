# jp2a

> 将JPEG图像转换为ASCII。
> 更多信息：<https://csl.name/jp2a/>.

- 从文件中读取JPEG图像并以ASCII格式打印：

`jp2a {{path/to/image.jpeg}}`

- 从URL中读取JPEG图像并以ASCII格式打印：

`jp2a {{www.example.com/image.jpeg}}`

- 为ASCII输出上色：

`jp2a --colors {{path/to/image.jpeg}}`

- 指定用于ASCII输出的字符：

`jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}`

- 将ASCII输出写入文件：

`jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}`

- 将ASCII输出写入HTML文件格式，适合在网页浏览器中查看：

`jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}`