# yaa

> 创建和操作 YAA 归档文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/yaa.1.html>.

- 从目录创建归档文件：

`yaa archive -d {{path/to/directory}} -o {{path/to/output_file.yaa}}`

- 从文件创建归档文件：

`yaa archive -i {{path/to/file}} -o {{path/to/output_file.yaa}}`

- 将归档文件解压到当前目录：

`yaa extract -i {{path/to/archive_file.yaa}}`

- 列出归档文件的内容：

`yaa list -i {{path/to/archive_file.yaa}}`

- 使用特定的压缩算法创建归档文件：

`yaa archive -a {{algorithm}} -d {{path/to/directory}} -o {{path/to/output_file.yaa}}`

- 使用 8 MB 块大小创建归档文件：

`yaa archive -b 8m -d {{path/to/directory}} -o {{path/to/output_file.yaa}}`
