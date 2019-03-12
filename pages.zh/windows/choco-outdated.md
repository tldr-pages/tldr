# choco outdated

> 使用Chocolatey检查过时的包.

- 用表格的形式列出过时的包:

`choco outdated`

- 忽略输出中的固定包:

`choco outdated --ignore-pinned`

- 从自定义的源处检查过时的包:

`choco outdated --source {{源URL|别名}}`

- 提供一个用户名和密码来进行验证:

`choco outdated --user {{username}} --password {{password}}`
