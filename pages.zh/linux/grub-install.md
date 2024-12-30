# grub-install

> 将 GRUB 安装到设备上。
> 更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>。

- 在 BIOS 系统上安装 GRUB：

`grub-install --target={{i386-pc}} {{path/to/device}}`

- 在 UEFI 系统上安装 GRUB：

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --bootloader-id={{GRUB}}`

- 安装 GRUB 并预加载特定模块：

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --modules="{{part_gpt part_msdos}}"`