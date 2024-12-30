# hashid

> Python3 程序，用于识别数据和密码哈希。
> 更多信息：<https://github.com/psypanda/hashID>。

- 从 `stdin` 中识别哈希（通过输入、复制粘贴或将哈希通过管道传入程序）：

`hashid`

- 识别一个或多个哈希：

`hashid {{hash1 hash2 ...}}`

- 识别文件中的哈希（每行一个哈希）：

`hashid {{path/to/hashes.txt}}`

- 显示所有可能的哈希类型（包括加盐哈希）：

`hashid --extended {{hash}}`

- 显示 `hashcat` 的模式编号和 `john` 的格式字符串：

`hashid --mode --john {{hash}}`

- 将输出保存到文件，而不是打印到 `stdout`：

`hashid --outfile {{path/to/output.txt}} {{hash}}`