# b2sum

> 计算 BLAKE2 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>。

- 计算一个或多个文件的 BLAKE2 校验和：

`b2sum {{path/to/file1 path/to/file2 ...}}`

- 计算并将 BLAKE2 校验和列表保存到文件中：

`b2sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b2}}`

- 从 `stdin` 计算 BLAKE2 校验和：

`{{command}} | b2sum`

- 阅读包含 BLAKE2 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`b2sum --check {{path/to/file.b2}}`

- 仅在缺少文件或验证失败时显示消息：

`b2sum --check --quiet {{path/to/file.b2}}`

- 仅在验证失败时显示消息，忽略缺少的文件：

`b2sum --ignore-missing --check --quiet {{path/to/file.b2}}`

- 检查已知文件的 BLAKE2 校验和：

`echo {{known_blake2_checksum_of_the_file}} {{path/to/file}} | b2sum --check`