# linode-cli domains

> 管理 Linode 域名和 DNS 配置。
> 参见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>。

- 列出所有管理的域名：

`linode-cli domains list`

- 创建一个新的管理域名：

`linode-cli domains create --domain {{domain_name}} --type {{master|slave}} --soa-email {{email}}`

- 查看特定域名的详细信息：

`linode-cli domains view {{domain_id}}`

- 删除一个管理的域名：

`linode-cli domains delete {{domain_id}}`

- 列出特定域名的记录：

`linode-cli domains records-list {{domain_id}}`

- 向域名添加一个 DNS 记录：

`linode-cli domains records-create {{domain_id}} --type {{A|AAAA|CNAME|MX|...}} --name {{subdomain}} --target {{target_value}}`

- 更新域名的 DNS 记录：

`linode-cli domains records-update {{domain_id}} {{record_id}} --target {{new_target_value}}`

- 从域名中删除一个 DNS 记录：

`linode-cli domains records-delete {{domain_id}} {{record_id}}`
