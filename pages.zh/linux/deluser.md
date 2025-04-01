# deluser

> 从系统中删除用户。
> 更多信息：<https://manned.org/deluser>.

- 删除用户：

`sudo deluser {{username}}`

- 删除用户及其主目录：

`sudo deluser --remove-home {{username}}`

- 删除用户及其主目录，但将用户的文件备份到指定目录中的 `.tar.gz` 文件中：

`sudo deluser --backup-to {{path/to/backup_directory}} --remove-home {{username}}`

- 删除用户及其拥有的一切文件：

`sudo deluser --remove-all-files {{username}}`