# choco search

> 使用 Chocolatey 搜索本地或远程软件包。
> 更多信息：<https://chocolatey.org/docs/commands-search>。

- 搜索软件包：

`choco search {{query}}`

- 本地搜索软件包：

`choco search {{query}} --local-only`

- 仅包含完全匹配的结果：

`choco search {{query}} --exact`

- 自动确认所有提示：

`choco search {{query}} --yes`

- 指定一个自定义源以搜索软件包：

`choco search {{query}} --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco search {{query}} --user {{username}} --password {{password}}`