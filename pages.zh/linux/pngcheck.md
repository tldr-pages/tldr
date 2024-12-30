# pngcheck

> 用于验证基于PNG（PNG、JNG、MNG）图像文件完整性的取证工具。
> 还可以从文件中提取嵌入的图像和文本。
> 更多信息：<http://www.libpng.org/pub/png/apps/pngcheck.html>。

- 验证图像文件的完整性：

`pngcheck {{path/to/file.png}}`

- 使用 [v]erbose 和 [c]olorized 输出检查文件：

`pngcheck -vc {{path/to/file.png}}`

- 显示 [t]ext 块的内容并 [s]earch 在特定文件内查找 PNG：

`pngcheck -ts {{path/to/file.png}}`

- 在特定文件内搜索并 e[x]tract 嵌入的 PNG：

`pngcheck -x {{path/to/file.png}}`