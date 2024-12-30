# namei

> 跟踪一个路径名（可以是符号链接），直到找到一个终端点（文件/目录/字符设备等）。
> 这个程序对于查找“符号链接层级过多”问题非常有用。
> 更多信息：<https://manned.org/namei>。

- 解析作为参数指定的路径名：

`namei {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 以长列表格式显示结果：

`namei --long {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 以 `ls` 风格显示每种文件类型的模式位：

`namei --modes {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 显示每个文件的所有者和组名：

`namei --owners {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 在解析时不跟踪符号链接：

`namei --nosymlinks {{path/to/a}} {{path/to/b}} {{path/to/c}}`