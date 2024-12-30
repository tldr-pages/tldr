# qlmanage

> QuickLook 服务器工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/qlmanage.1.html>。

- 显示一个或多个文件的 QuickLook：

`qlmanage -p {{path/to/file1 path/to/file2 ...}}`

- 计算当前目录中所有 JPEG 文件的 300 像素宽的 PNG 缩略图，并将它们放入一个目录：

`qlmanage {{*.jpg}} -t -s {{300}} {{path/to/directory}}`

- 重置 QuickLook：

`qlmanage -r`