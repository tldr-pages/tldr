# ldapdomaindump

> 通过 LDAP 导出用户、计算机、组、操作系统和成员关系信息到 HTML、JSON 和可搜索的输出格式。
> 另见 `ldapsearch`。
> 更多信息：<https://github.com/dirkjanm/ldapdomaindump>。

- 使用给定的 LDAP 帐户导出所有信息：

`ldapdomaindump --user {{domain}}\\{{administrator}} --password {{password|ntlm_hash}} {{hostname|ip}}`

- 导出所有信息，并解析计算机主机名：

`ldapdomaindump --resolve --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- 使用选定的 DNS 服务器解析计算机主机名并导出所有信息：

`ldapdomaindump --resolve --dns-server {{domain_controller_ip}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- 导出所有信息到指定目录，不生成 JSON 输出：

`ldapdomaindump --no-json --outdir {{path/to/directory}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`
