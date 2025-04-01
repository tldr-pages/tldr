# daps

> 一个用于将 DocBook XML 转换为 HTML 或 PDF 等输出格式的开源程序。
> 更多信息：<https://opensuse.github.io/daps/doc/index.html>。

- 检查 DocBook XML 文件是否有效：

`daps -d {{path/to/file.xml}} validate`

- 将 DocBook XML 文件转换为 PDF：

`daps -d {{path/to/file.xml}} pdf`

- 将 DocBook XML 文件转换为单个 HTML 文件：

`daps -d {{path/to/file.xml}} html --single`

- 显示帮助信息：

`daps --help`

- 显示版本信息：

`daps --version`