# b2sum

> 计算 BLAKE2 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>。

- 计算一个或多个文件的 BLAKE2 校验和：

`b2sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并保存 BLAKE2 校验和列表到文件：

`b2sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.b2}}`

- 从 `stdin` 计算 BLAKE2 校验和：

`{{命令}} | b2sum`

- 读取 BLAKE2 校验和文件并验证所有文件是否匹配：

`b2sum {{[-c|--check]}} {{路径/到/文件.b2}}`

- 仅对缺失文件或验证失败显示消息：

`b2sum {{[-c|--check]}} --quiet {{路径/到/文件.b2}}`

- 验证失败时显示消息，忽略缺失文件：

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{路径/到/文件.b2}}`

- 检查文件的已知 BLAKE2 校验和：

`echo {{文件的已知_blake2_校验和}} {{路径/到/文件}} | b2sum {{[-c|--check]}}`
