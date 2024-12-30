# pngcheck

> 打印有关 PNG、JNG 和 MNG 文件的详细信息并进行验证。
> 更多信息：<http://www.libpng.org/pub/png/apps/pngcheck.html>。

- 打印图像的摘要（宽度、高度和颜色深度）：

`pngcheck {{path/to/image.png}}`

- 以 [c]olorized 输出打印图像的信息：

`pngcheck -c {{path/to/image.png}}`

- 打印图像的 [v]erbose 信息：

`pngcheck -cvt {{path/to/image.png}}`

- 从 `stdin` 接收图像并显示详细信息：

`cat {{path/to/image.png}} | pngcheck -cvt`

- 在特定文件中 [s]earch PNG 并显示有关它们的信息：

`pngcheck -s {{path/to/image.png}}`

- 在另一个文件中搜索 PNG 并 [e]xtract 它们：

`pngcheck -x {{path/to/image.png}}`