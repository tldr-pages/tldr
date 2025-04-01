# snmpwalk

> SNMP 查询工具。
> 更多信息：<https://manned.org/snmpwalk>.

- 使用 SNMPv1 和社区字符串查询远程主机的系统信息：

`snmpwalk -v 1 -c {{community}} {{ip}}`

- 使用指定端口的 SNMPv2 通过 OID 查询远程主机的系统信息：

`snmpwalk -v 2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- 使用 SNMPv3 和认证但不加密通过 OID 查询远程主机的系统信息：

`snmpwalk -v 3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- 使用 SNMPv3、认证和加密通过 OID 查询远程主机的系统信息：

`snmpwalk -v 3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- 使用 SNMPv3 且不使用认证或加密通过 OID 查询远程主机的系统信息：

`snmpwalk -v 3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`

- 显示帮助：

`snmpwalk {{[-h|--help]}}`
