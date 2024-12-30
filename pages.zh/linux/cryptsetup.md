# cryptsetup

> 管理纯 `dm-crypt` 和 LUKS（Linux 统一密钥设置）加密卷。
> 一些子命令如 `luksFormat` 有其自己的使用文档。
> 更多信息：<https://manned.org/cryptsetup>。

- 使用密码初始化 LUKS 卷（覆盖分区上的所有数据）：

`cryptsetup luksFormat {{/dev/sdXY}}`

- 打开 LUKS 卷并在 `/dev/mapper/mapping_name` 创建一个解密映射：

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- 显示映射的信息：

`cryptsetup status {{mapping_name}}`

- 删除现有的映射：

`cryptsetup close {{mapping_name}}`

- 更改 LUKS 卷的密码：

`cryptsetup luksChangeKey {{/dev/sdXY}}`