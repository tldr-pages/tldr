# yadm transcrypt

> 如果已安装 `transcrypt`，此命令允许直接向 `transcrypt` 传递选项。
> 环境配置为使用 yadm 仓库。
> Transcrypt 使 Git 仓库中的文件能够透明地加密和解密。
> 更多信息：<https://github.com/elasticdog/transcrypt#command-line-options>.

- 设置用于加密的对称加密算法：

`yadm transcrypt --cipher={{加密算法}}`

- 提供用来派生密钥的密码：

`yadm transcrypt --password={{密码}}`

- 假设所有回答为“是”并接受未指定选项的默认值：

`yadm transcrypt --yes`

- 显示当前仓库的加密算法和密码：

`yadm transcrypt --display`

- 使用新的凭证重新加密所有已加密的文件：

`yadm transcrypt --rekey`
