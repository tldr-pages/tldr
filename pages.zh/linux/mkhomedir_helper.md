# mkhomedir_helper

> 在创建用户后创建用户的家目录。
> 更多信息：<https://manned.org/mkhomedir_helper>.

- 基于 `/etc/skel` 并使用 umask 022 创建用户的家目录：

`sudo mkhomedir_helper {{username}}`

- 基于 `/etc/skel` 并为所有者设置所有权限（0），并为组设置读权限（3）创建用户的家目录：

`sudo mkhomedir_helper {{username}} {{037}}`

- 基于自定义的骨架目录创建用户的家目录：

`sudo mkhomedir_helper {{username}} {{umask}} {{path/to/skeleton_directory}}`
