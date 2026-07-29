# sha256sum

> 计算 SHA256 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>。

- 计算一个或多个文件的 SHA256 校验和：

`sha256sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并保存 SHA256 校验和列表到文件：

`sha256sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.sha256}}`

- 从 `stdin` 计算 SHA256 校验和：

`{{命令}} | sha256sum`

- 读取 SHA256 校验和文件并验证所有文件是否匹配：

`sha256sum {{[-c|--check]}} {{路径/到/文件.sha256}}`

- 仅对缺失文件或验证失败显示消息：

`sha256sum {{[-c|--check]}} --quiet {{路径/到/文件.sha256}}`

- 验证失败时显示消息，忽略缺失文件：

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{路径/到/文件.sha256}}`

- 检查文件的已知 SHA256 校验和：

`echo {{文件的已知_sha256_校验和}} {{路径/到/文件}} | sha256sum {{[-c|--check]}}`
