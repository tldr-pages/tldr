# npm org

> 管理组织。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-org>.

- 将新用户添加到组织中：

`npm org set {{organization_name}} {{username}}`

- 更改用户在组织中的角色：

`npm org set {{organization_name}} {{username}} {{developer|admin|owner}}`

- 从组织中移除用户：

`npm org rm {{organization_name}} {{username}}`

- 列出组织中的所有用户：

`npm org ls {{organization_name}}`

- 列出组织中的所有用户，并以 JSON 格式输出：

`npm org ls {{organization_name}} --json`

- 显示用户在组织中的角色：

`npm org ls {{organization_name}} {{username}}`
