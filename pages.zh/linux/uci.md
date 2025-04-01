# uci

> 管理 OpenWrt 配置文件。
> 更多信息：<https://openwrt.org/docs/techref/uci>.

- 获取一个值：

`uci get {{network.lan.ipaddr}}`

- 列出所有选项及其值：

`uci show {{network}}`

- 设置一个值：

`uci set {{config}}.{{section}}.{{option}}={{value}}`

- 添加一个新的部分：

`uci add {{config}} {{section}}`

- 删除一个部分或值：

`uci delete {{config}}.{{section}}.{{option}}`

- 提交更改：

`uci commit {{config}}`

- 丢弃未提交的更改：

`uci revert {{config}}`

- 显示帮助：

`uci`
