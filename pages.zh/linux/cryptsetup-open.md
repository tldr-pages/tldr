# cryptsetup open

> 创建加密卷的解密映射。
> 注意：启用 TRIM 可能会导致少量数据泄露，如已释放块的信息，可能足以确定使用的文件系统。
> 但是，您仍然可能希望启用它，因为内部数据仍然是安全的，而没有 TRIM 的 SSD 会更快磨损。
> 更多信息：<https://manned.org/cryptsetup-open>.

- 打开一个 LUKS 卷，并在 `/dev/mapper/mapping_name` 创建解密映射：

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- 使用密钥文件而不是密码：

`cryptsetup open --key-file {{path/to/file}} {{/dev/sdXY}} {{mapping_name}}`

- 允许对设备使用 TRIM：

`cryptsetup open --allow-discards {{/dev/sdXY}} {{mapping_name}}`

- 将 `--allow-discards` 选项写入 LUKS 头（下次打开设备时将自动使用该选项）：

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{mapping_name}}`

- 打开一个 LUKS 卷并使解密映射为只读：

`cryptsetup open --readonly {{/dev/sdXY}} {{mapping_name}}`
