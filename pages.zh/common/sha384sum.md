# sha384sum

> 计算 SHA384 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>。

- 计算一个或多个文件的 SHA384 校验和：

`sha384sum {{path/to/file1 path/to/file2 ...}}`

- 计算并保存 SHA384 校验和列表到一个文件：

`sha384sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha384}}`

- 从 `stdin` 计算 SHA384 校验和：

`{{command}} | sha384sum`

- 读取一个包含 SHA384 校验和和文件名的文件，并验证所有文件的校验和：

`sha384sum {{[-c|--check]}} {{path/to/file.sha384}}`

- 仅在文件缺失或验证失败时显示消息：

`sha384sum {{[-c|--check]}} --quiet {{path/to/file.sha384}}`

- 仅在验证失败时显示消息，忽略缺失的文件：

`sha384sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha384}}`

- 验证文件的已知 SHA384 校验和：

`echo {{known_sha384_checksum_of_the_file}} {{path/to/file}} | sha384sum {{[-c|--check]}}`