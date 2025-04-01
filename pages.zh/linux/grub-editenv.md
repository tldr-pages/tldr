# grub-editenv

> 编辑 GRUB 环境变量。
> 更多信息：<https://www.gnu.org/software/grub/manual/grub/grub.html>.

- 设置默认启动项（假设启动项已存在）：

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- 显示 `timeout` 变量的当前值：

`grub-editenv /boot/grub/grubenv list timeout`

- 将 `saved_entry` 变量重置为默认值：

`grub-editenv /boot/grub/grubenv unset saved_entry`

- 在内核命令行末尾追加 "quiet splash"：

`grub-editenv /boot/grub/grubenv set kernel_cmdline="$kernel_cmdline quiet splash"`