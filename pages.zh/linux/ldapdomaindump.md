# ldapdomaindump

> 通过LDAP将用户、计算机、组、操作系统和成员信息导出为HTML、JSON和可grep的输出。
> 另见 `ldapsearch`。
> 更多信息：<https://github.com/dirkjanm/ldapdomaindump>。

- 使用给定的LDAP帐户导出所有信息：

`ldapdomaindump --user {{domain}}\\{{administrator}} --password {{password|ntlm_hash}} {{hostname|ip}}`

- 导出所有信息，解析计算机主机名：

`ldapdomaindump --resolve --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- 导出所有信息，使用选定的DNS服务器解析计算机主机名：

`ldapdomaindump --resolve --dns-server {{domain_controller_ip}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- 将所有信息导出到指定目录，不生成JSON输出：

`ldapdomaindump --no-json --outdir {{path/to/directory}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`