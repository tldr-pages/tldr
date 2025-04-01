# ldapsearch

> 查询 LDAP 目录。
> 更多信息：<https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html>.

- 查询 LDAP 服务器，查找给定组的所有成员，并返回对象的 displayName 值：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- 使用无换行符密码文件查询 LDAP 服务器，查找给定组的所有成员，并返回对象的 displayName 值：

`ldapsearch -D '{{admin_DN}}' -y '{{password_file}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- 返回符合给定过滤条件的 5 个条目：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -z 5 displayName`

- 最多等待 7 秒以获取响应：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -l 7 displayName`

- 反转过滤条件：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '(!(memberOf={{group1}}))' displayName`

- 返回属于多个组的所有条目，并返回每个条目的显示名称：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- 返回属于指定组中至少一个组的所有条目：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- 组合多个布尔逻辑过滤条件：

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
