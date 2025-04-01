# detox

> 重命名文件以使其更容易处理。
> 它会移除空格和其他令人烦恼的字符，如重复的下划线。
> 更多信息：<https://github.com/dharple/detox>。

- 移除文件名中的空格和其他不希望存在的字符：

`detox {{path/to/file}}`

- 显示 detox 将如何重命名目录树中的所有文件：

`detox --dry-run -r {{path/to/directory}}`

- 移除目录树中所有文件名中的空格和其他不希望存在的字符：

`detox -r {{path/to/directory}}`
