# yadm-transcrypt

> 如果安装了 `transcrypt`，此命令允许您直接将选项传递给 `transcrypt`。
> 在配置为使用 yadm 仓库的环境中。
> Transcrypt 允许对 Git 仓库中的文件进行透明加密和解密。
> 更多信息：<https://github.com/elasticdog/transcrypt>。

- 设置用于加密的对称加密算法：

`yadm transcrypt --cipher={{cipher}}`

- 传递用于派生密钥的密码：

`yadm transcrypt --password={{password}}`

- 假设为“是”，并接受未指定选项的默认值：

`yadm transcrypt --yes`

- 显示当前仓库的加密算法和密码：

`yadm transcrypt --display`

- 使用新凭据重新加密所有已加密文件：

`yadm transcrypt --rekey`