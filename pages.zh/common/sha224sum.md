# sha224sum

> 计算 SHA224 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 计算一个或多个文件的 SHA224 校验和：

`sha224sum {{path/to/file1 path/to/file2 ...}}`

- 计算并保存 SHA224 校验和列表到文件：

`sha224sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha224}}`

- 从 `stdin` 计算 SHA224 校验和：

`{{command}} | sha224sum`

- 读取 SHA224 校验和文件和文件名，验证所有文件的校验和是否匹配：

`sha224sum {{[-c|--check]}} {{path/to/file.sha224}}`

- 仅在文件缺失或验证失败时显示消息：

`sha224sum {{[-c|--check]}} --quiet {{path/to/file.sha224}}`

- 仅在验证失败时显示消息，忽略缺失的文件：

`sha224sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha224}}`

- 检查已知的文件 SHA224 校验和：

`echo {{known_sha224_checksum_of_the_file}} {{path/to/file}} | sha224sum {{[-c|--check]}}`
