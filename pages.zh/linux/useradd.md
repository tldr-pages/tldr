# useradd

> 创建新用户。
> 参见：`users`, `userdel`, `usermod`。
> 更多信息：<https://manned.org/useradd>。

- 创建新用户：

`sudo useradd {{username}}`

- 创建具有指定用户ID的新用户：

`sudo useradd {{[-u|--uid]}} {{id}} {{username}}`

- 创建具有指定shell的新用户：

`sudo useradd {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- 创建属于附加组的新用户（注意没有空格）：

`sudo useradd {{[-G|--groups]}} {{group1,group2,...}} {{username}}`

- 创建具有默认主目录的新用户：

`sudo useradd {{[-m|--create-home]}} {{username}}`

- 创建具有由模板目录文件填充的主目录的新用户：

`sudo useradd {{[-k|--skel]}} {{path/to/template_directory}} {{[-m|--create-home]}} {{username}}`

- 创建没有主目录的新系统用户：

`sudo useradd {{[-r|--system]}} {{username}}`
