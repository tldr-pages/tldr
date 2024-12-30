# cryptsetup luksFormat

> 使用密码或密钥文件初始化 LUKS 分区和初始密钥插槽 (0)。
> 注意：此操作将覆盖分区上的所有数据。
> 更多信息：<https://manned.org/cryptsetup-luksFormat>。

- 使用密码初始化 LUKS 卷：

`cryptsetup luksFormat {{/dev/sdXY}}`

- 使用密钥文件初始化 LUKS 卷：

`cryptsetup luksFormat {{/dev/sdXY}} {{path/to/keyfile}}`

- 使用密码初始化 LUKS 卷并设置其标签：

`cryptsetup luksFormat --label {{label}} {{/dev/sdXY}}`