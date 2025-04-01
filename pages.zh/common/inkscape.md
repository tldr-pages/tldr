# inkscape

> 一个用于编辑 SVG（可缩放矢量图形）的程序。
> 对于 Inkscape 0.92.x 及更早版本，请使用 -e 代替 -o。
> 更多信息：<https://inkscape.org>。

- 在 Inkscape GUI 中打开一个 SVG 文件：

`inkscape {{path/to/filename.svg}}`

- 将 SVG 文件导出为位图，默认格式为 PNG，默认分辨率为 96 DPI：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}}`

- 将 SVG 文件导出为 600x400 像素的位图（可能会发生纵横比失真）：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}} -w {{600}} -h {{400}}`

- 将 SVG 文件中的绘图（所有对象的边界框）导出为位图：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}} -D`

- 根据对象的 ID 将单个对象导出为位图：

`inkscape {{path/to/filename.svg}} -i {{id}} -o {{object.png}}`

- 将 SVG 文档导出为 PDF，并将所有文本转换为路径：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.pdf}} --export-text-to-path`

- 复制 ID 为 "path123" 的对象，将副本旋转 90 度，保存文件并退出 Inkscape：

`inkscape {{path/to/filename.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
