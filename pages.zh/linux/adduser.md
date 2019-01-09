# adduser

> 添加用户的工具.

- 创建一个新用户,在默认路径创建home目录,并提示用户设置密码:

`adduser {{用户名}}`

- 创建一个新用户,不生成home目录:

`adduser --no-create-home {{用户名}}`

- 创建一个新用户,并在指定路径下创建home目录:

`adduser --home {{home路径}} {{用户名}}`

- 创建一个新用户,并指定登录shell:

`adduser --shell {{shell路径}} {{用户名}}`

- 创建一个新用户,并指定其用户组:

`adduser --ingroup {{用户组}} {{用户名}}`
