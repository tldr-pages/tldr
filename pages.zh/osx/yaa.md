# yaa

> 创建和操作 YAA 归档文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/yaa.1.html>。

- 从目录创建归档：

`yaa archive -d {{路径/到/目录}} -o {{路径/到/输出文件.yaa}}`

- 从文件创建归档：

`yaa archive -i {{路径/到/文件}} -o {{路径/到/输出文件.yaa}}`

- 将归档提取到当前目录：

`yaa extract -i {{路径/到/归档文件.yaa}}`

- 列出归档的内容：

`yaa list -i {{路径/到/归档文件.yaa}}`

- 使用特定的压缩算法创建归档：

`yaa archive -a {{算法}} -d {{路径/到/目录}} -o {{路径/到/输出文件.yaa}}`

- 使用 8 MB 块大小创建归档：

`yaa archive -b 8m -d {{路径/到/目录}} -o {{路径/到/输出文件.yaa}}`