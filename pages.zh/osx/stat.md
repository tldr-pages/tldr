# stat

> 显示文件状态。
> 更多信息：<https://keith.github.io/xcode-man-pages/stat.1.html>.

- 显示文件属性，如大小、权限、创建和访问日期等：

`stat {{文件}}`

- 与上面相同，但更详细（更类似于 Linux 的 `stat`）：

`stat -x {{文件}}`

- 只显示文件权限：

`stat -f %Mp%Lp {{文件}}`

- 显示文件的所有者和所属组：

`stat -f "%Su %Sg" {{文件}}`

- 以字节为单位显示文件的大小：

`stat -f "%z %N" {{文件}}`
