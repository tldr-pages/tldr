# stat

> 显示文件状态。
> 更多信息：<https://keith.github.io/xcode-man-pages/stat.1.html>。

- 显示文件属性，例如大小、权限、创建和访问日期等：

`stat {{path/to/file}}`

- 与上述相同，但更详细（更类似于Linux的`stat`）：

`stat -x {{path/to/file}}`

- 仅显示八进制文件权限：

`stat -f %Mp%Lp {{path/to/file}}`

- 显示文件的所有者和组：

`stat -f "%Su %Sg" {{path/to/file}}`

- 显示文件的大小（以字节为单位）：

`stat -f "%z %N" {{path/to/file}}`