# snmpbulkget

> 查询 MIB 树中的下一个值及其所有相邻值。
> 更多信息：<https://manned.org/snmpbulkget>.

- 向 SNMP 代理请求下一个值：

`snmpbulkget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- 显示完整的对象标识符（OID）路径：

`snmpbulkget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`

- 显示帮助：

`snmpbulkget {{[-h|--help]}}`
