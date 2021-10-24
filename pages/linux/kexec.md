# kexec

> Directly reboot into a new kernel.
> More information: <https://manned.org/kexec>.

- Load a new kernel:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --command-line={{arguments}}`

- Load a new kernel with current boot parameters:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --reuse-cmdline`

- Execute a currently loaded kernel:

`kexec -e`

- Unload current kexec target kernel:

`kexec -u`
