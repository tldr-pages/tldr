# 打开

> 打开文件、目录和应用程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/open.1.html>。

- 使用关联的应用程序打开文件：

`open {{file.ext}}`

- 运行图形化的 macOS [a]pplication：

`open -a "{{Application}}"`

- 根据 [b]undle 标识符运行图形化的 macOS 应用程序（参考 `osascript` 获取此标识符的简单方法）：

`open -b {{com.domain.application}}`

- 在 Finder 中打开当前目录：

`open .`

- [R]eveal 在 Finder 中显示文件：

`open -R {{path/to/file}}`

- 使用关联的应用程序打开当前目录下所有给定扩展名的文件：

`open {{*.ext}}`

- 打开指定 [b]undle 标识符的应用程序的新实例：

`open -n -b {{com.domain.application}}`