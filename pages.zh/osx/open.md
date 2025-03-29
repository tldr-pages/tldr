# open

> 打开文件、目录和应用程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/open.1.html>.

- 使用系统关联的应用程序打开文件：

`open {{文件名.扩展名}}`

- 运行图形化的 macOS 应用程序：

`open -a "{{应用程序名}}"`

- 运行指定包标识符的图形化 macOS 应用程序（请参阅`OSascript`命令，查询如何获取应用程序的包标识符）：

`open -b {{com.domain.application}}`

- 在"访达（finder）"中打开当前文件夹：

`open .`

- 打开"访达（finder）", 并且给出指定文件：

`open -R {{路径/到/文件}}`

- 使用系统默认应用程序，打开当前目录中所有给定扩展名的文件：

`open {{*.扩展名}}`

- 通过包标识符打开应用程序的新实例：

`open -n -b {{com.domain.application}}`
