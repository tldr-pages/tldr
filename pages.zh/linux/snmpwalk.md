# snmpwalk

> SNMP 查询工具。
> 更多信息：<https://manned.org/snmpwalk>。

- 使用 SNMPv1 和社区字符串查询远程主机的系统信息：

`snmpwalk -v1 -c {{community}} {{ip}}`

- 使用 SNMPv2 在指定端口通过 OID 查询远程主机的系统信息：

`snmpwalk -v2c -c {{community}} {{ip}}:{{port}} {{oid}}`

- 使用 SNMPv3 和无加密认证通过 OID 查询远程主机的系统信息：

`snmpwalk -v3 -l {{authNoPriv}} -u {{username}} -a {{MD5|SHA}} -A {{passphrase}} {{ip}} {{oid}}`

- 使用 SNMPv3、认证和加密通过 OID 查询远程主机的系统信息：

`snmpwalk -v3 -l {{authPriv}} -u {{username}} -a {{MD5|SHA}} -A {{auth_passphrase}} -x {{DES|AES}} -X {{enc_passphrase}} {{ip}} {{oid}}`

- 使用 SNMPv3，无认证或加密通过 OID 查询远程主机的系统信息：

`snmpwalk -v3 -l {{noAuthNoPriv}} -u {{username}} {{ip}} {{oid}}`