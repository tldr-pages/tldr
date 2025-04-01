# fastd

> 虚拟专用网络守护进程。
> 支持二层或三层，支持多种加密方法，由 Freifunk 使用。
> 参见: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`。
> 更多信息: <https://fastd.readthedocs.io/en/stable/>。

- 使用特定配置文件启动 `fastd`：

`fastd --config {{path/to/fastd.conf}}`

- 使用 1400 的 MTU 启动三层 VPN，并从文件中加载其余配置参数：

`fastd --mode {{tap}} --mtu {{1400}} --config {{path/to/fastd.conf}}`

- 验证配置文件：

`fastd --verify-config --config {{path/to/fastd.conf}}`

- 生成新的密钥对：

`fastd --generate-key`

- 显示配置文件中私钥对应的公钥：

`fastd --show-key --config {{path/to/fastd.conf}}`

- 显示当前版本：

`fastd -v`