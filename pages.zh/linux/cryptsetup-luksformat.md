# cryptsetup luksFormat

> 初始化 LUKS 分区并使用口令或密钥文件初始化密钥槽位（0）。
> 注意：此操作将覆写分区上的所有数据。
> 更多信息：<https://manned.org/cryptsetup-luksFormat>.

- 使用口令初始化 LUKS 卷：

`cryptsetup luksFormat {{/dev/sdXY}}`

- 使用密钥文件初始化 LUKS 卷：

`cryptsetup luksFormat {{/dev/sdXY}} {{路径/到/密钥文件}}`

- 使用口令初始化 LUKS 卷并设置其标签：

`cryptsetup luksFormat --label {{标签}} {{/dev/sdXY}}`
