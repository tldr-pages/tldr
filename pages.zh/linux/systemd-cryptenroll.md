# systemd-cryptenroll

> 交互式注册或移除用于解锁 LUKS2 加密设备的方法。除非另有指定，否则使用密码解锁设备。
> 为了允许分区在系统启动时解锁，需要更新 `/etc/crypttab` 文件或 initramfs。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- 注册新密码（类似于 `cryptsetup luksAddKey`）:

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- 注册新恢复密钥（即随机生成的可以作为备用的密码）:

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- 列出可用的令牌，或注册新 PKCS#11 令牌:

`systemd-cryptenroll --pkcs11-token-uri {{list|auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- 列出可用的 FIDO2 设备，或注册新 FIDO2 设备（当只插入一个令牌时，可以使用 `auto` 作为设备名称）:

`systemd-cryptenroll --fido2-device {{list|auto|path/to/fido2_hidraw_device}} {{path/to/luks2_block_device}}`

- 注册支持用户验证（生物识别）的新 FIDO2 设备:

`systemd-cryptenroll --fido2-device {{auto|path/to/fido2_hidraw_device}} --fido2-with-user-verification yes {{path/to/luks2_block_device}}`

- 使用 FIDO2 设备解锁，并注册新 FIDO2 设备:

`systemd-cryptenroll --unlock-fido2-device {{path/to/fido2_hidraw_unlock_device}} --fido2-device {{path/to/fido2_hidraw_enroll_device}} {{path/to/luks2_block_device}}`

- 注册 TPM2 安全芯片（仅支持安全启动策略 PCR），并要求额外的字母数字 PIN 码:

`systemd-cryptenroll --tpm2-device {{auto|path/to/tpm2_block_device}} --tpm2-with-pin yes {{path/to/luks2_block_device}}`

- 移除所有空密码/所有密码/所有 FIDO2 设备/所有 PKCS#11 令牌/所有 TPM2 安全芯片/所有恢复密钥/所有方法:

`systemd-cryptenroll --wipe-slot {{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{path/to/luks2_block_device}}`