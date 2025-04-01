# setfile

> 在 HFS+ 目录中的文件上设置文件属性。
> 更多信息：<https://ss64.com/osx/setfile.html>.

- 为特定文件设置创建日期：

`setfile -d "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- 为特定文件设置修改日期：

`setfile -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- 为符号链接文件设置修改日期（而不是链接的文件本身）：

`setfile -P -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`