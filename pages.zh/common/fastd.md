# fastd

> VPN 守护进程。
> 在第 2 层或第 3 层工作，支持不同的加密方法，供 Freifunk 使用。
> 另见：`ivpn`，`mozillavpn`，`mullvad`，`warp-cli`。
> 更多信息：<https://fastd.readthedocs.io/en/stable/>。

- 使用特定的配置文件启动 `fastd`：

`fastd --config {{path/to/fastd.conf}}`

- 启动一个 MTU 为 1400 的第 3 层 VPN，从文件中加载其余的配置参数：

`fastd --mode {{tap}} --mtu {{1400}} --config {{path/to/fastd.conf}}`

- 验证配置文件：

`fastd --verify-config --config {{path/to/fastd.conf}}`

- 生成一个新的密钥对：

`fastd --generate-key`

- 显示配置文件中私钥的公钥：

`fastd --show-key --config {{path/to/fastd.conf}}`

- 显示当前版本：

`fastd -v`