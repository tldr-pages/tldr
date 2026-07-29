# shred

> 覆盖文件以安全删除数据。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>。

- 覆盖文件：

`shred {{路径/到/文件}}`

- 覆盖文件并在屏幕上显示进度：

`shred {{[-v|--verbose]}} {{路径/到/文件}}`

- 覆盖文件，留下零而不是随机数据：

`shred {{[-z|--zero]}} {{路径/到/文件}}`

- 覆盖文件特定次数：

`shred {{[-n|--iterations]}} {{25}} {{路径/到/文件}}`

- 覆盖文件并删除它：

`shred {{[-u|--remove]}} {{路径/到/文件}}`

- 覆盖文件 100 次，最后用零覆盖，删除文件，并显示详细进度：

`shred {{[-vzu|--verbose --zero --remove]}} {{[-n|--iterations]}} 100 {{路径/到/文件}}`
