# shasum

> 计算 SHA 加密校验和。
> 更多信息：<https://manned.org/shasum>。

- 计算一个或多个文件的 SHA1 校验和：

`shasum {{path/to/file1 path/to/file2 ...}}`

- 使用指定算法计算一个或多个文件的 SHA 校验和：

`shasum --algorithm {{1|224|256|384|512|512224|512256}} {{path/to/file1 path/to/file2 ...}}`

- 从 `stdin` 计算 SHA1 校验和：

`{{command}} | shasum`

- 计算并将 SHA256 校验和列表保存到文件：

`shasum --algorithm 256 {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha256}}`

- 读取一个包含 SHA 校验和和文件名的文件，并验证所有文件的校验和是否匹配（算法将自动检测）：

`shasum --check {{path/to/file}}`

- 仅在缺失文件或验证失败时显示消息：

`shasum --check --quiet {{path/to/file}}`

- 仅在验证失败时显示消息，忽略缺失文件：

`shasum --ignore-missing --check --quiet {{path/to/file}}`

- 检查文件的已知 SHA 校验和：

`echo {{known_sha_checksum_of_the_file}} {{path/to/file}} | shasum --check`