# sha1sum

> 计算 SHA1 哈希校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>.

- 计算一个或多个文件的 SHA1 校验和：

`sha1sum {{path/to/file1 path/to/file2 ...}}`

- 计算 SHA1 校验和并将结果保存到文件中：

`sha1sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha1}}`

- 从 `stdin` 计算 SHA1 校验和：

`{{command}} | sha1sum`

- 读取包含 SHA1 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`sha1sum {{[-c|--check]}} {{path/to/file.sha1}}`

- 仅当文件缺失或验证失败时显示消息：

`sha1sum {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- 仅当验证失败时显示消息，忽略缺失的文件：

`sha1sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- 验证文件的已知 SHA1 校验和：

`echo {{known_sha1_checksum_of_the_file}} {{path/to/file}} | sha1sum {{[-c|--check]}}`
