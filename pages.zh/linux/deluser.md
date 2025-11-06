# deluser

> 从系统中删除用户。
> 更多信息：<https://manned.org/deluser>.

- 删除用户：

`sudo deluser {{用户名}}`

- 删除用户及其主目录：

`sudo deluser --remove-home {{用户名}}`

- 删除用户及其主目录，但将其文件备份到指定目录中的 .tar.gz 文件：

`sudo deluser --backup-to {{路径/到/备份目录}} --remove-home {{用户名}}`

- 删除用户及其所有拥有的文件：

`sudo deluser --remove-all-files {{用户名}}`
