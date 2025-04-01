# finger

> 用户信息查询程序。
> 更多信息：<https://manned.org/finger>.

- 显示当前登录用户的信息：

`finger`

- 显示特定用户的信息：

`finger {{username}}`

- 显示用户的登录名、真实姓名、终端名等信息：

`finger -s`

- 以多行格式输出，显示与 `-s` 相同的信息，以及用户的家目录、家庭电话、登录 shell、邮件状态等信息：

`finger -l`

- 防止匹配用户名，仅使用登录名：

`finger -m`