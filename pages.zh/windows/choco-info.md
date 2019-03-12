# choco info

> 显示有关Chocolatey包的详细信息.

- 显示指定包的信息:

`choco info {{包名}}`

- 显示一个本地已安装包的信息:

`choco info {{包名}} --local-only`

- 从一个自定义的源来获取包的信息:

`choco info {{包名}} --source {{源URL|别名}}`

- 提供一个用户名和密码来进行验证:

`choco info {{包名}} --user {{用户名}} --password {{密码}}`
