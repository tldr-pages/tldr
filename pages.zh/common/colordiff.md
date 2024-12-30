# colordiff

> 一个围绕 `diff` 的包装器，产生相同的输出，但具有美观的语法高亮。
> 颜色方案可以自定义。
> 更多信息：<https://github.com/kimmel/colordiff>。

- 比较文件：

`colordiff {{file1}} {{file2}}`

- 以两列输出：

`colordiff -y {{file1}} {{file2}}`

- 忽略文件内容中的大小写差异：

`colordiff -i {{file1}} {{file2}}`

- 报告两个文件是否相同：

`colordiff -s {{file1}} {{file2}}`

- 忽略空白：

`colordiff -w {{file1}} {{file2}}`