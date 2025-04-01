# salt-key

> 管理 Salt 主服务器上的 Salt Minion 密钥。
> 需要在 Salt 主服务器上以 root 用户或使用 sudo 运行。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>.

- 列出所有已接受、未接受和已拒绝的 Minion 密钥：

`salt-key -L`

- 按名称接受一个 Minion 密钥：

`salt-key -a {{MINION_ID}}`

- 按名称拒绝一个 Minion 密钥：

`salt-key -r {{MINION_ID}}`

- 打印所有公钥的指纹：

`salt-key -F`
