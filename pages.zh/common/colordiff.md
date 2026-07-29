# colordiff

> `diff` 的包装器，产生相同的输出但带有漂亮的语法高亮。
> 颜色方案可以自定义。
> 更多信息：<https://manned.org/colordiff>。

- 比较文件：

`colordiff {{文件1}} {{文件2}}`

- 以两列输出：

`colordiff -y {{文件1}} {{文件2}}`

- 忽略文件内容中的大小写差异：

`colordiff -i {{文件1}} {{文件2}}`

- 报告两个文件何时相同：

`colordiff -s {{文件1}} {{文件2}}`

- 忽略空白字符：

`colordiff -w {{文件1}} {{文件2}}`
