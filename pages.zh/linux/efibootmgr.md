# efibootmgr

> 操作 UEFI 启动管理器。
> 更多信息：<https://manned.org/efibootmgr>。

- 列出所有启动选项及其编号：

`efibootmgr {{-u|--unicode}}`

- 将 UEFI Shell v2 添加为启动选项：

`sudo efibootmgr -c -d {{/dev/sda}} -p {{1}} -l "{{\path\to\shell.efi}}" -L "{{UEFI Shell}}"`

- 将 Linux 添加为启动选项：

`sudo efibootmgr --create --disk {{/dev/sda}} --part {{1}} --loader "{{\vmlinuz}}" --unicode "{{kernel_cmdline}}" --label "{{Linux}}"`

- 更改当前启动顺序：

`sudo efibootmgr {{-o|--bootorder}} {{0002,0008,0001,0005}}`

- 删除一个启动选项：

`sudo efibootmgr {{-b|--bootnum}} {{0008}} {{-B|--delete-bootnum}}`