# md5sum

> 计算 MD5 加密校验和。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- 计算一个或多个文件的 MD5 校验和：

`md5sum {{路径/到/文件1 路径/到/文件2 ...}}`

- 计算并将 MD5 校验和列表保存到一个文件中：

`md5sum {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/文件.md5}}`

- 从 `stdin` 计算 MD5 校验和：

`{{命令}} | md5sum`

- 读取包含 MD5 校验和和文件名的文件，并验证所有文件的校验和是否匹配：

`md5sum --check {{路径/到/文件.md5}}`

- 仅在文件丢失或验证失败时显示消息：

`md5sum --check --quiet {{路径/到/文件.md5}}`

- 仅在验证失败时显示消息，忽略丢失的文件：

`md5sum --ignore-missing --check --quiet {{路径/到/文件.md5}}`

- 检查已知文件的 MD5 校验和：

`echo {{已知的文件的_md5_校验和}} {{路径/到/文件}} | md5sum --check`
