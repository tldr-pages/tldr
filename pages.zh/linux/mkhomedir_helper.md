# mkhomedir_helper

> 在创建用户后创建用户的主目录。
> 更多信息：<https://manned.org/mkhomedir_helper>。

- 根据 `/etc/skel` 创建用户的主目录，umask 为 022：

`sudo mkhomedir_helper {{用户名}}`

- 根据 `/etc/skel` 创建用户的主目录，所有者拥有所有权限（0），组拥有读权限（3）：

`sudo mkhomedir_helper {{用户名}} {{037}}`

- 基于自定义骨架创建用户的主目录：

`sudo mkhomedir_helper {{用户名}} {{umask}} {{路径/到/骨架目录}}`