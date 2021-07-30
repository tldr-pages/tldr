# grub-install

> 安装GRUB到设备.
> 更多信息: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- 安装GRUB到基于BIOS的系统:

`grub-install --target={{i386-pc}} {{path/to/device}}`

- 安装GRUB到基于UEFI的系统:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --bootloader-id={{GRUB}}`

- 安装预置指定模块的GRUB:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --modules="{{part_gpt part_msdos}}"`
