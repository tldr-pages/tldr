# pio 组织

> 管理 PlatformIO 组织及其所有者。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/org/>。

- 创建一个新组织：

`pio org create {{organization_name}}`

- 删除一个组织：

`pio org destroy {{organization_name}}`

- 向组织添加用户：

`pio org add {{organization_name}} {{username}}`

- 从组织中移除用户：

`pio org remove {{organization_name}} {{username}}`

- 列出当前用户是成员的所有组织及其所有者：

`pio org list`

- 更新组织的名称、电子邮件或显示名称：

`pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}`