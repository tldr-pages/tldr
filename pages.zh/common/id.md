# id

> 显示当前用户和组的身份信息。
> 另请参阅：`logname`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html>。

- 显示当前用户的 ID（UID）、组 ID（GID）及所属组：

`id`

- 显示当前用户的身份：

`id {{[-un|--user --name]}}`

- 以数字形式显示当前用户的身份：

`id {{[-u|--user]}}`

- 显示当前主组的身份：

`id {{[-gn|--group --name]}}`

- 以数字形式显示当前主组的身份：

`id {{[-g|--group]}}`

- 显示当前用户所属的所有组：

`id {{[-Gn|--groups --name]}}`

- 显示任意用户的 ID（UID）、组 ID（GID）及所属组：

`id {{用户名}}`

- 跳过名称查找，直接指定 UID 编号：

`id +{{uid_编号}}`
