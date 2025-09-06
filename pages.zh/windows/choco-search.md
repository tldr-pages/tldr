# choco search

> 使用 Chocolatey 搜索一个本地或远程的包。
> 更多信息：<https://chocolatey.org/docs/commands-search>.

- 搜索一个包：

`choco search {{查询语句}}`

- 搜索一个本地的包：

`choco search {{查询语句}} --local-only`

- 只显示包含完全匹配的结果：

`choco search {{查询语句}} --exact`

- 自动确认所有提示：

`choco search {{查询语句}} --yes`

- 从自定义的源处搜索包：

`choco search {{查询语句}} --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco search {{查询语句}} --user {{用户名}} --password {{密码}}`
