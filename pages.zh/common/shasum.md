# shasum

> 计算或检查加密 SHA 校验值。
> 更多信息：<https://manned.org/shasum>.

- 计算文件的 SHA1 校验值：

`shasum {{文件名}}`

- 计算文件的 SHA256 校验值：

`shasum --algorithm 256 {{文件名}}`

- 计算多个文件的 SHA512 校验值：

`shasum --algorithm 512 {{文件名 1}} {{文件名 2}}`

- 计算一个文件内列出的所有的目录文件的相对应的总数：

`shasum --check {{列表文件}}`

- 从标准输入中获取并计算 SHA1 校验值：

`{{其他命令}} | shasum`
