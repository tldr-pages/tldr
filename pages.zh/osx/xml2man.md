# xml2man

> 将 MPGL 编译为 mdoc。
> 更多信息：<https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>。

- 将 MPGL 文件编译为可查看的手册页：

`xml2man {{path/to/command_file.mxml}}`

- 将 MPGL 文件编译为指定的输出文件：

`xml2man {{path/to/service_file.mxml}} {{path/to/service_file.7}}`

- 将 MPGL 文件编译为指定的输出文件，如果已存在则覆盖：

`xml2man -f {{path/to/function_file.mxml}} {{path/to/function_file.3}}`
