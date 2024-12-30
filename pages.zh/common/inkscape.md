# inkscape

> 一个 SVG（可缩放矢量图形）编辑程序。
> 对于 Inkscape 版本到 0.92.x，请使用 -e 而不是 -o。
> 更多信息：<https://inkscape.org>。

- 在 Inkscape GUI 中打开一个 SVG 文件：

`inkscape {{path/to/filename.svg}}`

- 将 SVG 文件导出为位图，使用默认格式（PNG）和默认分辨率（96 DPI）：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}}`

- 将 SVG 文件导出为 600x400 像素的位图（可能会发生宽高比失真）：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}} -w {{600}} -h {{400}}`

- 将 SVG 文件的图形（所有对象的边界框）导出为位图：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.png}} -D`

- 导出具有特定 ID 的单个对象为位图：

`inkscape {{path/to/filename.svg}} -i {{id}} -o {{object.png}}`

- 将 SVG 文档导出为 PDF，将所有文本转换为路径：

`inkscape {{path/to/filename.svg}} -o {{path/to/filename.pdf}} --export-text-to-path`

- 复制 ID 为 "path123" 的对象，旋转复制品 90 度，保存文件并退出 Inkscape：

`inkscape {{path/to/filename.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`