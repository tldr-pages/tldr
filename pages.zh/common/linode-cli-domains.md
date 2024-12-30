# linode-cli 域

> 管理 Linode 域和 DNS 配置。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>。

- 列出所有管理的域：

`linode-cli domains list`

- 创建一个新的管理域：

`linode-cli domains create --domain {{domain_name}} --type {{master|slave}} --soa-email {{email}}`

- 查看特定域的详细信息：

`linode-cli domains view {{domain_id}}`

- 删除一个管理域：

`linode-cli domains delete {{domain_id}}`

- 列出特定域的记录：

`linode-cli domains records-list {{domain_id}}`

- 向域添加 DNS 记录：

`linode-cli domains records-create {{domain_id}} --type {{A|AAAA|CNAME|MX|...}} --name {{subdomain}} --target {{target_value}}`

- 更新域的 DNS 记录：

`linode-cli domains records-update {{domain_id}} {{record_id}} --target {{new_target_value}}`

- 从域删除 DNS 记录：

`linode-cli domains records-delete {{domain_id}} {{record_id}}`