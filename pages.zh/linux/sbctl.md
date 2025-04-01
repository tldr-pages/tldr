# sbctl

> 一个用户友好的安全启动密钥管理工具。
> 注意：不注册 Microsoft 的证书可能会 brick 你的系统。更多详情见：<https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>。
> 更多信息：<https://github.com/Foxboron/sbctl#usage>。

- 显示当前的安全启动状态：

`sbctl status`

- 创建自定义的安全启动密钥（默认情况下，所有内容都存储在 `/var/lib/sbctl`）：

`sbctl create-keys`

- 注册自定义的安全启动密钥和 Microsoft 的 UEFI 厂商证书：

`sbctl enroll-keys --microsoft`

- 根据 `/etc/sbctl/sbctl.conf` 中的设置自动运行 `create-keys` 和 `enroll-keys`：

`sbctl setup --setup`

- 使用创建的密钥签名一个 EFI 二进制文件，并将文件保存到数据库中：

`sbctl sign {{[-s|--save]}} {{path/to/efi_binary}}`

- 重新签名所有已保存的文件：

`sbctl sign-all`

- 验证 EFI 系统分区上的所有 EFI 可执行文件是否已签名：

`sbctl verify`