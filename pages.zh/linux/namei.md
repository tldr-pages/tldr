# namei

> 跟踪路径名（可以是符号链接），直到找到终端点（文件/目录/字符设备等）。
> 该程序对于查找“符号链接层数过多”的问题非常有用。
> 更多信息：<https://manned.org/namei>.

- 解析作为参数指定的路径名：

`namei {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 以长列表格式显示结果：

`namei {{[-l|--long]}} {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 以 `ls` 的方式显示每个文件类型的权限位：

`namei {{[-m|--modes]}} {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 显示每个文件的所有者和组名：

`namei {{[-o|--owners]}} {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- 解析过程中不跟随符号链接：

`namei {{[-n|--nosymlinks]}} {{path/to/a}} {{path/to/b}} {{path/to/c}}`