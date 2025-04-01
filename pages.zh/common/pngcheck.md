# pngcheck

> 用于验证基于 PNG（PNG、JNG、MNG）图像文件的完整性。
> 也可以从文件中提取嵌入的图像和文本。
> 更多信息：<https://github.com/pnggroup/pngcheck>。

- 验证图像文件的完整性（宽度、高度和颜色深度）：

`pngcheck {{path/to/image.png}}`

- 以彩色输出的方式打印图像的信息：

`pngcheck -c {{path/to/image.png}}`

- 打印图像的详细信息：

`pngcheck -cvt {{path/to/image.png}}`

- 从 `stdin` 接收图像并显示详细信息：

`cat {{path/to/image.png}} | pngcheck -cvt`

- 在指定文件中搜索 PNG 图像并显示相关信息：

`pngcheck -s {{path/to/image.png}}`

- 在另一个文件中搜索 PNG 图像并提取它们：

`pngcheck -x {{path/to/image.png}}`
