# kcadm.sh

> 执行管理任务。
> 更多信息：<https://www.keycloak.org/docs/latest/server_admin/#admin-cli>。

- 开始一个已认证的会话：

`kcadm.sh config credentials --server {{host}} --realm {{realm_name}} --user {{username}} --password {{password}}`

- 创建一个用户：

`kcadm.sh create users -s username={{username}} -r {{realm_name}}`

- 列出所有领域：

`kcadm.sh get realms`

- 使用 JSON 配置更新领域：

`kcadm.sh update realms/{{realm_name}} -f {{path/to/file.json}}`
