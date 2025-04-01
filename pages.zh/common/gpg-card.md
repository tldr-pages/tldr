# gpg-card

> 管理 OpenPGP 和 PIV 智能卡。
> 类似于 `gpg --card-edit`。
> 更多信息：<https://manned.org/gpg-card>。

- 以交互模式启动：

`gpg-card`

- 非交互式执行一个或多个命令：

`gpg-card {{command1}} -- {{command2}} -- {{command3}}`

- 显示智能卡的信息：

`gpg-card list`

- 使用存储在 OpenPGP 卡上的 URL 获取公钥：

`gpg-card fetch`

- 设置 `fetch` 命令使用的 URL：

`gpg-card url`

- 更改或解锁 PIN（在非交互模式下使用卡的默认操作）：

`gpg-card passwd`

- 切换 OpenPGP 卡的 forcesig 标志（即要求输入用户 PIN 以进行签名）：

`gpg-card forcesig`

- 智能卡出厂重置（即删除所有数据并重置 PIN）：

`gpg-card factory-reset`
