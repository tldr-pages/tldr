# efibootmgr

> 操纵 UEFI 引导管理器。
> 更多信息：<https://manned.org/efibootmgr>.

- 列出所有引导选项及其编号：

`efibootmgr {{[-u|--unicode]}}`

- 添加 UEFI Shell v2 为引导选项：

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{\path\to\shell.efi}}" {{[-L|--label]}} "{{UEFI Shell}}"`

- 添加 Linux 为引导选项：

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{\vmlinuz}}" {{[-u|--unicode]}} "{{kernel_cmdline}}" {{[-L|--label]}} "{{Linux}}"`

- 更改当前的引导顺序：

`sudo efibootmgr {{[-o|--bootorder]}} {{0002,0008,0001,0005}}`

- 删除一个引导选项：

`sudo efibootmgr {{[-b|--bootnum]}} {{0008}} {{[-B|--delete-bootnum]}}`
