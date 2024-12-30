# systemd-cryptsetup

> 创建或移除加密卷的解密映射。相当于 `cryptsetup open` 和 `cryptsetup close`。
> 此命令的参数格式与 `/etc/crypttab` 中的一行完全相同。它被 systemd 用于在启动时解锁设备。
> 另请参见：`cryptsetup`。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-cryptsetup.html>。

- 打开一个 LUKS 卷并在 `/dev/mapper/mapping_name` 创建一个解密映射：

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}}`

- 使用额外选项打开一个 LUKS 卷并在 `/dev/mapper/mapping_name` 创建一个解密映射：

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} none {{crypttab_options}}`

- 使用密钥文件打开一个 LUKS 卷并在 `/dev/mapper/mapping_name` 创建一个解密映射：

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} {{path/to/keyfile}} {{crypttab_options}}`

- 移除现有映射：

`systemd-cryptsetup detach {{mapping_name}}`