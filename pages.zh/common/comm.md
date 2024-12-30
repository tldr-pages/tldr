# comm

> 选择或拒绝两个文件中的共同行。两个文件必须已排序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>。

- 生成三列以制表符分隔的内容：仅在第一个文件中的行，仅在第二个文件中的行和共同的行：

`comm {{file1}} {{file2}}`

- 仅打印两个文件中共同的行：

`comm -12 {{file1}} {{file2}}`

- 仅打印两个文件中共同的行，从 `stdin` 读取一个文件：

`cat {{file1}} | comm -12 - {{file2}}`

- 获取仅在第一个文件中找到的行，将结果保存到第三个文件中：

`comm -23 {{file1}} {{file2}} > {{file1_only}}`

- 打印仅在第二个文件中找到的行，当文件未排序时：

`comm -13 <(sort {{file1}}) <(sort {{file2}})`