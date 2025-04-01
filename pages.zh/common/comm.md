# comm

> 选择或排除两个文件中的公共行。两个文件都必须是已排序的。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

- 生成三个以制表符分隔的列：仅在第一个文件中的行，仅在第二个文件中的行，以及两个文件共有的行：

`comm {{file1}} {{file2}}`

- 仅打印两个文件共有的行：

`comm -12 {{file1}} {{file2}}`

- 仅打印两个文件共有的行，其中一个文件从 `stdin` 读取：

`cat {{file1}} | comm -12 - {{file2}}`

- 获取仅在第一个文件中找到的行，将结果保存到第三个文件中：

`comm -23 {{file1}} {{file2}} > {{file1_only}}`

- 当文件未排序时，仅打印在第二个文件中找到的行：

`comm -13 <(sort {{file1}}) <(sort {{file2}})`
