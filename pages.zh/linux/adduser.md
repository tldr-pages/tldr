# adduser

> 添加用户的工具。
> 更多信息：<https://manpages.debian.org/latest/adduser/adduser.html>.

- 创建一个新用户，在默认路径创建 home 目录，并提示用户设置密码：

`adduser {{用户名}}`

- 创建一个新用户，不生成 home 目录：

`adduser --no-create-home {{用户名}}`

- 创建一个新用户，并在指定路径下创建 home 目录：

`adduser --home {{home 路径}} {{用户名}}`

- 创建一个新用户，并指定登录 shell:

`adduser --shell {{shell 路径}} {{用户名}}`

- 创建一个新用户，并指定其用户组：

`adduser --ingroup {{用户组}} {{用户名}}`

- 将一个现有用户加入指定用户组：

`adduser {{用户名}} {{用户组}}`
