# b3sum

> 计算 BLAKE3 加密校验和。
> 更多信息：<https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>。

- 计算一个或多个文件的 BLAKE3 校验和：

`b3sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并保存 BLAKE3 校验和列表到文件：

`b3sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.b3}}`

- 从 `stdin` 计算 BLAKE3 校验和：

`{{命令}} | b3sum`

- 读取 BLAKE3 校验和文件并验证所有文件是否匹配：

`b3sum {{[-c|--check]}} {{路径/到/文件.b3}}`

- 仅对缺失文件或验证失败显示消息：

`b3sum {{[-c|--check]}} --quiet {{路径/到/文件.b3}}`

- 检查文件的已知 BLAKE3 校验和：

`echo {{文件的已知_blake3_校验和}} {{路径/到/文件}} | b3sum {{[-c|--check]}}`
