# open

> 打开文件、目录和应用程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/open.1.html>.

- 使用系统关联的应用程序打开文件：

`open {{filename.extension}}`

- 运行图形化的 macOS 应用程序：

`open -a {{应用程序名}}`

- 运行指定 包名 的图形化 macOS 应用程序（请参阅`OSascript`命令，查询如何获取应用程序的 包名）：

`open -b {{com.domain.application 应用程序包名}}`

- 在"访达（finder）"中打开当前文件夹：

`open .`

- 打开"访达（finder）", 并且给出指定文件：

`open -R {{文件路径}}`

- 使用系统默认应用程序，打开当前目录中所有给定扩展名的文件：

`open {{*.extension}}`
