# cryptsetup open

> 创建一个加密卷的解密映射。
> 注意：启用 TRIM 后，可能会出现最小的数据泄漏，表现为已释放块信息，这可能足以确定正在使用的文件系统。
> 然而，您仍然很可能希望启用它，因为内部数据仍然安全，并且不启用 TRIM 的 SSD 会更快磨损。
> 更多信息：<https://manned.org/cryptsetup-open>。

- 打开一个 LUKS 卷并在 `/dev/mapper/mapping_name` 创建一个解密映射：

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- 使用密钥文件而不是密码短语：

`cryptsetup open --key-file {{path/to/file}} {{/dev/sdXY}} {{mapping_name}}`

- 允许在设备上使用 TRIM：

`cryptsetup open --allow-discards {{/dev/sdXY}} {{mapping_name}}`

- 将 `--allow-discards` 选项写入 LUKS 头（该选项将在您打开设备时始终使用）：

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{mapping_name}}`

- 打开一个 LUKS 卷并将解密映射设置为只读：

`cryptsetup open --readonly {{/dev/sdXY}} {{mapping_name}}`