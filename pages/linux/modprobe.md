# modprobe

> Add or remove modules from the Linux kernel.
> See also: `lsmod`, `kmod`.
> More information: <https://manned.org/modprobe>.

- Simulate loading a module into the kernel:

`modprobe {{[-n|--dry-run]}} {{module_name}}`

- Load a module into the kernel:

`sudo modprobe {{module_name}}`

- Load multiple modules:

`sudo modprobe {{[-a|--all]}} {{module_name1 module_name2 ...}}`

- Remove a module from the kernel:

`sudo modprobe {{[-r|--remove]}} {{module_name}}`

- Remove a module and those that depend on it from the kernel:

`sudo modprobe {{[-r|--remove]}} --remove-holders {{module_name}}`

- Show a kernel module's dependencies:

`sudo modprobe {{[-D|--show-depends]}} {{module_name}}`
