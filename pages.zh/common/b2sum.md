# b2sum

> 计算 BLAKE2 哈希值。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- 计算一个或多个文件的 BLAKE2 哈希值：

`b2sum {{path/to/file1 path/to/file2 ...}}`

- 计算并保存 BLAKE2 哈希值列表到文件：

`b2sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b2}}`

- 从 `stdin` 计算 BLAKE2 哈希值：

`{{command}} | b2sum`

- 读取 BLAKE2 哈希值和文件名列表并验证所有文件的哈希值是否匹配：

`b2sum {{[-c|--check]}} {{path/to/file.b2}}`

- 仅在文件丢失或验证失败时显示消息：

`b2sum {{[-c|--check]}} --quiet {{path/to/file.b2}}`

- 仅在验证失败时显示消息，忽略丢失的文件：

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.b2}}`

- 检查已知的文件 BLAKE2 哈希值：

`echo {{known_blake2_checksum_of_the_file}} {{path/to/file}} | b2sum {{[-c|--check]}}`