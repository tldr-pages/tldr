# grub-install

> 安装 GRUB 到设备。
> 更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- 安装 GRUB 到基于 BIOS 的系统：

`grub-install --target={{i386-pc}} {{/dev/sdX}}`

- 安装 GRUB 到基于 UEFI 的系统：

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --bootloader-id={{GRUB}}`

- 安装预置指定模块的 GRUB：

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --modules="{{part_gpt part_msdos}}"`
