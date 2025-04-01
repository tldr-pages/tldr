# while

> 简单的 shell 循环，当返回值为零时重复执行。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- 从 `stdin` 读取并针对每一行执行操作：

`while read line; do echo "$line"; done`

- 每秒执行一次命令，无限循环：

`while :; do {{command}}; sleep 1; done`

- 执行命令直到它失败：

`while {{command}}; do :; done`
