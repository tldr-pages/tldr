# grub-file

> 检查文件是否为可启动映像类型。
> 更多信息：<https://manned.org/grub-file>.

- 检查文件是否为 ARM EFI 映像：

`grub-file --is-arm-efi {{path/to/file}}`

- 检查文件是否为 i386 EFI 映像：

`grub-file --is-i386-efi {{path/to/file}}`

- 检查文件是否为 x86_64 EFI 映像：

`grub-file --is-x86_64-efi {{path/to/file}}`

- 检查文件是否为 ARM 映像（Linux 内核）：

`grub-file --is-arm-linux {{path/to/file}}`

- 检查文件是否为 x86 映像（Linux 内核）：

`grub-file --is-x86-linux {{path/to/file}}`

- 检查文件是否为 x86_64 XNU 映像（macOS 内核）：

`grub-file --is-x86_64-xnu {{path/to/file}}`
