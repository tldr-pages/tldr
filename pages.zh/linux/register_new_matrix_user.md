# register_new_matrix_user

> 在用户注册已禁用的情况下，在主服务器中注册新用户。
> 更多信息：<https://manned.org/register_new_matrix_user>.

- 交互式创建用户：

`register_new_matrix_user --config {{path/to/homeserver.yaml}}`

- 交互式创建管理员用户：

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --admin`

- 非交互式创建管理员用户（不推荐）：

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --user {{username}} --password {{password}} --admin`
