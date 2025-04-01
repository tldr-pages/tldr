# colordiff

> `diff` 的包装器，产生相同输出但带有漂亮的语法高亮。
> 可以自定义颜色方案。
> 更多信息：<https://github.com/kimmel/colordiff>。

- 比较文件：

`colordiff {{file1}} {{file2}}`

- 以两列形式输出：

`colordiff -y {{file1}} {{file2}}`

- 忽略文件内容中的大小写差异：

`colordiff -i {{file1}} {{file2}}`

- 当两个文件相同时报告：

`colordiff -s {{file1}} {{file2}}`

- 忽略空白字符：

`colordiff -w {{file1}} {{file2}}`
