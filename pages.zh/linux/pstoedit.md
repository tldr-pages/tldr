# pstoedit

> 将PDF文件转换为各种图像格式。
> 更多信息：<http://www.pstoedit.net>。

- 将PDF页面转换为PNG或JPEG格式：

`pstoedit -page {{页面编号}} -f magick {{文件路径/file.pdf}} {{页面.png|页面.jpg}}`

- 将多个PDF页面转换为编号图像：

`pstoedit -f magick {{文件路径}} {{页面%d.png|页面%d.jpg}}`