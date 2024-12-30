# adduser

> 用户添加工具。
> 更多信息：<https://manned.org/adduser>。

- 创建一个新的用户，默认的主目录，并提示用户设置密码：

`adduser {{用户名}}`

- 创建一个没有主目录的新用户：

`adduser --no-create-home {{用户名}}`

- 创建一个在指定路径下的主目录的新用户：

`adduser --home {{主目录路径}} {{用户名}}`

- 创建一个将指定的shell设置为登录shell的新用户：

`adduser --shell {{shell路径}} {{用户名}}`

- 创建一个属于指定组的新用户：

`adduser --ingroup {{组}} {{用户名}}`