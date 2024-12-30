# 获取文件信息

> 获取 HFS+ 目录中一个文件的信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/GetFileInfo.1.html>。

- 显示给定文件的信息：

`GetFileInfo {{path/to/file}}`

- 显示给定文件的创建[时]间和日期：

`GetFileInfo -d {{path/to/file}}`

- 显示给定文件的最后[修]改时间和日期：

`GetFileInfo -m {{path/to/file}}`

- 显示给定文件的[创]作者：

`GetFileInfo -c {{path/to/file}}`