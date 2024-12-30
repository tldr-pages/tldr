# bleachbit

> 清理文件系统上的垃圾文件。
> 更多信息：<https://docs.bleachbit.org/doc/command-line-interface.html>。

- 启动Bleachbit的图形用户界面（GUI）版本：

`bleachbit --gui`

- 擦除一个文件：

`bleachbit --shred {{path/to/file}}`

- 列出可用的清理选项：

`bleachbit --list-cleaners`

- 在实际执行清理操作之前，预览将被删除的文件和将要进行的其他更改：

`bleachbit --preview {{--preset|cleaner1.option1 cleaner2.* ...}}`

- 执行清理操作并删除文件：

`bleachbit --clean {{--preset|cleaner1.option1 cleaner2.* ...}}`