# b3sum

> 计算 BLAKE3 加密校验和。
> 更多信息：<https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- 计算一个或多个文件的 BLAKE3 校验和：

`b3sum {{path/to/file1 path/to/file2 ...}}`

- 计算并将 BLAKE3 校验和列表保存到文件中：

`b3sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.b3}}`

- 从 `stdin` 计算 BLAKE3 校验和：

`{{command}} | b3sum`

- 读取包含 BLAKE3 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`b3sum {{[-c|--check]}} {{path/to/file.b3}}`

- 仅在文件缺失或验证失败时显示消息：

`b3sum {{[-c|--check]}} --quiet {{path/to/file.b3}}`

- 验证文件的已知 BLAKE3 校验和：

`echo {{known_blake3_checksum_of_the_file}} {{path/to/file}} | b3sum {{[-c|--check]}}`