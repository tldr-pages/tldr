# sha256sum

> 计算 SHA256 加密校验和。
> 更多信息： <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 计算一个或多个文件的 SHA256 校验和：

`sha256sum {{path/to/file1 path/to/file2 ...}}`

- 计算并保存 SHA256 校验和列表到文件中：

`sha256sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha256}}`

- 从 `stdin` 计算 SHA256 校验和：

`{{command}} | sha256sum`

- 读取包含 SHA256 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`sha256sum {{[-c|--check]}} {{path/to/file.sha256}}`

- 仅在文件丢失或验证失败时显示消息：

`sha256sum {{[-c|--check]}} --quiet {{path/to/file.sha256}}`

- 仅在验证失败时显示消息，忽略丢失的文件：

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha256}}`

- 检查文件的已知 SHA256 校验和：

`echo {{known_sha256_checksum_of_the_file}} {{path/to/file}} | sha256sum {{[-c|--check]}}`
