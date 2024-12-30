# sha1sum

> 计算SHA1加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/sha1sum>。

- 计算一个或多个文件的SHA1校验和：

`sha1sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并将SHA1校验和列表保存到文件中：

`sha1sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.sha1}}`

- 从`stdin`计算SHA1校验和：

`{{命令}} | sha1sum`

- 读取SHA1校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`sha1sum --check {{路径/到/文件.sha1}}`

- 仅在缺少文件或验证失败时显示消息：

`sha1sum --check --quiet {{路径/到/文件.sha1}}`

- 仅在验证失败时显示消息，忽略缺少的文件：

`sha1sum --ignore-missing --check --quiet {{路径/到/文件.sha1}}`

- 检查文件的已知SHA1校验和：

`echo {{已知文件的_sha1校验和}} {{路径/到/文件}} | sha1sum --check`