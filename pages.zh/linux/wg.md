# wg

> 管理 WireGuard 接口的配置。
> 更多信息：<https://www.wireguard.com/quickstart/>.

- 检查当前活动接口的状态：

`sudo wg`

- 生成一个新的私钥：

`wg genkey`

- 从私钥生成公钥：

`wg pubkey < {{path/to/private_key}} > {{path/to/public_key}}`

- 生成公钥和私钥：

`wg genkey | tee {{path/to/private_key}} | wg pubkey > {{path/to/public_key}}`

- 显示 wireguard 接口的当前配置：

`sudo wg showconf {{wg0}}`