# adduser

> 添加用户的工具.

- 创建一个新用户,在默认路径创建home目录,并提示用户设置密码

`adduser {{username}}`

- 创建一个新用户,不生成home目录:

`adduser --no-create-home {{username}}`

- 创建一个新用户,并在指定路径下创建home目录

`adduser --home {{path/to/home}} {{username}}`

- 创建一个新用户,并指定登录shell

`adduser --shell {{path/to/shell}} {{username}}`

- 创建一个新用户,并指定其用户组

`adduser --ingroup {{group}} {{username}}`
