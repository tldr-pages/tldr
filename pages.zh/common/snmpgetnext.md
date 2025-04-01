# snmpgetnext

> 查询 MIB 树中的下一个值。
> 更多信息：<https://manned.org/snmpgetnext>。

- 向 SNMP 代理请求下一个值：

`snmpgetnext -v {{version}} -c {{community}} {{ip}} {{oid}}`

- 显示完整的对象标识符（OID）路径：

`snmpgetnext -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`

- 显示帮助：

`snmpgetnext {{[-h|--help]}}`
