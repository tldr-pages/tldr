# sha512sum

> 计算 SHA512 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 计算一个或多个文件的 SHA512 校验和：

`sha512sum {{path/to/file1 path/to/file2 ...}}`

- 计算并保存 SHA512 校验和列表到一个文件：

`sha512sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha512}}`

- 从 `stdin` 计算 SHA512 校验和：

`{{command}} | sha512sum`

- 读取一个包含 SHA512 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`sha512sum {{[-c|--check]}} {{path/to/file.sha512}}`

- 仅在文件缺失或验证失败时显示消息：

`sha512sum {{[-c|--check]}} --quiet {{path/to/file.sha512}}`

- 仅在验证失败时显示消息，忽略缺失的文件：

`sha512sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha512}}`

- 检查已知的文件 SHA512 校验和：

`echo {{known_sha512_checksum_of_the_file}} {{path/to/file}} | sha512sum {{[-c|--check]}}`
