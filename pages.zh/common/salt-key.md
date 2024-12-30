# salt-key

> 在盐主机上管理盐从机密钥。
> 需要在盐主机上运行，可能需要以 root 用户身份或使用 sudo。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>。

- 列出所有已接受、未接受和被拒绝的从机密钥：

`salt-key -L`

- 按名称接受一个从机密钥：

`salt-key -a {{MINION_ID}}`

- 按名称拒绝一个从机密钥：

`salt-key -r {{MINION_ID}}`

- 打印所有公钥的指纹：

`salt-key -F`