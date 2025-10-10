# modprobe

> Add or remove modules from the Linux kernel.
> See also: `kmod` for other module management commands.
> More information: <https://manned.org/modprobe>.

- Pretend to load a module into the kernel, but don't actually do it:

`sudo modprobe {{[-n|--dry-run]}} {{module_name}}`

- Load a module into the kernel:

`sudo modprobe {{module_name}}`

- Remove a module from the kernel:

`sudo modprobe {{[-r|--remove]}} {{module_name}}`

- Remove a module and those that depend on it from the kernel:

`sudo modprobe {{[-r|--remove]}} --remove-holders {{module_name}}`

- Show a kernel module's dependencies:

`sudo modprobe {{[-D|--show-depends]}} {{module_name}}`
