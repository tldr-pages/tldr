# sha384sum

> 计算SHA384加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>。

- 计算一个或多个文件的SHA384校验和：

`sha384sum {{path/to/file1 path/to/file2 ...}}`

- 计算并将SHA384校验和列表保存到文件：

`sha384sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha384}}`

- 从`stdin`计算SHA384校验和：

`{{command}} | sha384sum`

- 读取一个SHA384校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`sha384sum --check {{path/to/file.sha384}}`

- 仅在缺少文件或验证失败时显示消息：

`sha384sum --check --quiet {{path/to/file.sha384}}`

- 仅在验证失败时显示消息，忽略缺失的文件：

`sha384sum --ignore-missing --check --quiet {{path/to/file.sha384}}`

- 检查文件的已知SHA384校验和：

`echo {{known_sha384_checksum_of_the_file}} {{path/to/file}} | sha384sum --check`