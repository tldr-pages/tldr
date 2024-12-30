# md5sum

> 计算 MD5 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>。

- 计算一个或多个文件的 MD5 校验和：

`md5sum {{path/to/file1 path/to/file2 ...}}`

- 计算并将 MD5 校验和列表保存到文件中：

`md5sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.md5}}`

- 从 `stdin` 计算 MD5 校验和：

`{{command}} | md5sum`

- 读取一个包含 MD5 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`md5sum --check {{path/to/file.md5}}`

- 仅在缺少文件或验证失败时显示消息：

`md5sum --check --quiet {{path/to/file.md5}}`

- 仅在验证失败时显示消息，忽略缺少的文件：

`md5sum --ignore-missing --check --quiet {{path/to/file.md5}}`

- 检查一个已知文件的 MD5 校验和：

`echo {{known_md5_checksum_of_the_file}} {{path/to/file}} | md5sum --check`