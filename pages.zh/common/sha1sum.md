# sha1sum

> 计算 SHA1 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>。

- 计算一个或多个文件的 SHA1 校验和：

`sha1sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并保存 SHA1 校验和列表到文件：

`sha1sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.sha1}}`

- 从 `stdin` 计算 SHA1 校验和：

`{{命令}} | sha1sum`

- 读取 SHA1 校验和文件并验证所有文件是否匹配：

`sha1sum {{[-c|--check]}} {{路径/到/文件.sha1}}`

- 仅对缺失文件或验证失败显示消息：

`sha1sum {{[-c|--check]}} --quiet {{路径/到/文件.sha1}}`

- 验证失败时显示消息，忽略缺失文件：

`sha1sum --ignore-missing {{[-c|--check]}} --quiet {{路径/到/文件.sha1}}`

- 检查文件的已知 SHA1 校验和：

`echo {{文件的已知_sha1_校验和}} {{路径/到/文件}} | sha1sum {{[-c|--check]}}`
