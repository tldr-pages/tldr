# cat

> 打印和拼接文件的工具。
> 更多信息：<https://www.gnu.org/software/coreutils/cat>.

- 以标准输出，打印文件内容：

`cat {{file}}`

- 多文件合并到目标文件：

`cat {{file1}} {{file2}} > {{target_file}}`

- 多文件合并，并追加到目标文件：

`cat {{file1}} {{file2}} >> {{target_file}}`

- 显示行号：

`cat -n {{file}}`

- 显示不可打印和空白的字符（使用 `M-` 前缀标记非 ASCII 字符）：

`cat -v -t -e {{file}}`
