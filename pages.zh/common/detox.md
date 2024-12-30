# detox

> 重命名文件以便更容易处理。
> 它会去除空格和其他令人烦恼的字符，比如重复的下划线字符。
> 更多信息：<https://github.com/dharple/detox>。

- 从文件名中移除空格和其他不需要的字符：

`detox {{path/to/file}}`

- 显示 detox 将如何重命名目录树中的所有文件：

`detox --dry-run -r {{path/to/directory}}`

- 从目录树中的所有文件中移除空格和其他不需要的字符：

`detox -r {{path/to/directory}}`