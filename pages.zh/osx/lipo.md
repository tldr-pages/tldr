# lipo

> 处理 Mach-O 通用二进制文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/lipo.1.html>。

- 从两个单架构文件创建通用文件：

`lipo {{path/to/binary_file.x86_64}} {{path/to/binary_file.arm64e}} -create -output {{path/to/binary_file}}`

- 列出通用文件中包含的所有架构：

`lipo {{path/to/binary_file}} -archs`

- 显示通用文件的详细信息：

`lipo {{path/to/binary_file}} -detailed_info`

- 从通用文件中提取单架构文件：

`lipo {{path/to/binary_file}} -thin {{arm64e}} -output {{path/to/binary_file.arm64e}}`