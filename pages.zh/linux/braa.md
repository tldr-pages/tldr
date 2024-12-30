# braa

> 超快速的批量 SNMP 扫描器，能够同时处理多个主机。
> 更多信息：<https://github.com/mteg/braa>。

- 使用公共字符串查询 `.1.3.6` 下的所有 OID，遍历主机的 SNMP 树：

`braa public@{{ip}}:{{.1.3.6.*}}`

- 查询整个子网 `ip_range` 的 `system.sysLocation.0`：

`braa public@{{ip_range}}:{{.1.3.6.1.2.1.1.6.0}}`

- 尝试将 `system.sysLocation.0` 的值设置为特定的工作组：

`braa private@{{ip}}:{{.1.3.6.1.2.1.1.6.0}}=s'{{workgroup}}'`