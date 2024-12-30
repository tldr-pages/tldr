# systemd-cryptenroll

> 交互式注册或移除用于解锁LUKS2加密设备的方法。使用密码解锁设备，除非另有说明。
> 为了允许在系统启动期间解锁分区，请更新`/etc/crypttab`文件或initramfs。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>。

- 注册一个新密码（类似于`cryptsetup luksAddKey`）：

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- 注册一个新的恢复密钥（即可以作为备用的随机生成的密码短语）：

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- 列出可用的令牌，或注册一个新的PKCS#11令牌：

`systemd-cryptenroll --pkcs11-token-uri {{list|auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- 列出可用的FIDO2设备，或注册一个新的FIDO2设备（当只有一个令牌插入时，可以使用`auto`作为设备名称）：

`systemd-cryptenroll --fido2-device {{list|auto|path/to/fido2_hidraw_device}} {{path/to/luks2_block_device}}`

- 注册一个带有用户验证（生物识别）的新FIDO2设备：

`systemd-cryptenroll --fido2-device {{auto|path/to/fido2_hidraw_device}} --fido2-with-user-verification yes {{path/to/luks2_block_device}}`

- 使用FIDO2设备解锁，并注册一个新的FIDO2设备：

`systemd-cryptenroll --unlock-fido2-device {{path/to/fido2_hidraw_unlock_device}} --fido2-device {{path/to/fido2_hidraw_enroll_device}} {{path/to/luks2_block_device}}`

- 注册一个TPM2安全芯片（仅限安全启动策略PCR）并要求额外的字母数字PIN：

`systemd-cryptenroll --tpm2-device {{auto|path/to/tpm2_block_device}} --tpm2-with-pin yes {{path/to/luks2_block_device}}`

- 移除所有空密码/所有密码/所有FIDO2设备/所有PKCS#11令牌/所有TPM2安全芯片/所有恢复密钥/所有方法：

`systemd-cryptenroll --wipe-slot {{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{path/to/luks2_block_device}}`