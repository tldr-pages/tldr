# wg

> 管理 WireGuard 接口配置。
> 更多信息：<https://www.wireguard.com/quickstart/>.

- 检查当前激活接口的状态：

`sudo wg`

- 生成新的私钥：

`wg genkey`

- 从私钥生成公钥：

`wg pubkey < {{路径/到/私钥}} > {{路径/到/公钥}}`

- 同时生成公钥和私钥：

`wg genkey | tee {{路径/到/私钥}} | wg pubkey > {{路径/到/公钥}}`

- 展示 WireGuard 接口的当前配置：

`sudo wg showconf {{wg0}}`
