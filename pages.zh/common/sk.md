# sk

> 用Rust编写的模糊查找器。
> 类似于`fzf`。
> 更多信息：<https://github.com/lotabout/skim>。

- 在指定目录的所有文件上启动`skim`：

`find {{path/to/directory}} -type f | sk`

- 启动`skim`以查看运行中的进程：

`ps aux | sk`

- 使用指定查询启动`skim`：

`sk --query "{{query}}"`

- 使用`Shift + Tab`选择多个文件并写入文件：

`find {{path/to/directory}} -type f | sk --multi > {{path/to/file}}`