# sf

> 一个强大的命令行界面，可简化在您的 Salesforce 组织中进行开发和构建自动化的过程。
> 更多信息：<https://developer.salesforce.com/tools/salesforcecli>。

- 授权一个 Salesforce 组织：

`sf force:auth:web:login --setalias {{organization}} --instanceurl {{organization_url}}`

- 列出所有已授权的组织：

`sf force:org:list`

- 在默认网页浏览器中打开特定组织：

`sf force:org:open --targetusername {{organization}}`

- 显示特定组织的信息：

`sf force:org:display --targetusername {{organization}}`

- 将源元数据推送到组织：

`sf force:source:push --targetusername {{organization}}`

- 从组织中拉取源元数据：

`sf force:source:pull --targetusername {{organization}}`

- 为组织的登录用户生成一个密码：

`sf force:user:password:generate --targetusername {{organization}}`

- 为组织的登录用户分配一个权限集：

`sf force:user:permset:assign --permsetname {{permission_set_name}} --targetusername {{organization}}`