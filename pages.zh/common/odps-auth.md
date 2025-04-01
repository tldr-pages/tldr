# odps auth

> ODPS（开放数据处理服务）中的用户权限。
> 请参阅 `odps`。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 将用户添加到当前项目：

`add user {{username}};`

- 授予用户一组权限：

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};`

- 显示用户的权限：

`show grants for {{username}};`

- 创建用户角色：

`create role {{role_name}};`

- 授予角色一组权限：

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- 描述角色的权限：

`desc role {{role_name}};`

- 将角色授予用户：

`grant {{role_name}} to {{username}};`
