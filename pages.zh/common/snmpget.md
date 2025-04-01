# snmpget

> 使用 SNMP 协议查询。
> 更多信息：<https://manned.org/snmpget>.

- 从 SNMP 代理请求单个值：

`snmpget -v {{version}} -c {{community}} {{ip}} {{oid}}`

- 显示完整的对象标识符（OID）路径：

`snmpget -v {{version}} -c {{community}} -O f {{ip}} {{oid}}`

- 显示帮助：

`snmpget {{[-h|--help]}}`
