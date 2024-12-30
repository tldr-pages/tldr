# useradd

> 创建一个新用户。
> 另请参见：`users`，`userdel`，`usermod`。
> 更多信息：<https://manned.org/useradd>。

- 创建一个新用户：

`sudo useradd {{用户名}}`

- 创建一个具有指定用户 ID 的新用户：

`sudo useradd {{-u|--uid}} {{id}} {{用户名}}`

- 创建一个具有指定 shell 的新用户：

`sudo useradd {{-s|--shell}} {{路径/到/shell}} {{用户名}}`

- 创建一个属于附加组的新用户（注意没有空格）：

`sudo useradd {{-G|--groups}} {{组1,组2,...}} {{用户名}}`

- 创建一个具有默认主目录的新用户：

`sudo useradd {{-m|--create-home}} {{用户名}}`

- 创建一个主目录由模板目录文件填充的新用户：

`sudo useradd {{-k|--skel}} {{路径/到/模板目录}} {{-m|--create-home}} {{用户名}}`

- 创建一个没有主目录的新系统用户：

`sudo useradd {{-r|--system}} {{用户名}}`