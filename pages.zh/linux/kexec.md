# kexec

> 直接重启到新内核。
> 更多信息：<https://manned.org/kexec>.

- 加载新内核：

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --command-line={{arguments}}`

- 使用当前启动参数加载新内核：

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --reuse-cmdline`

- 执行已加载的内核：

`kexec -e`

- 卸载当前 kexec 目标内核：

`kexec -u`
