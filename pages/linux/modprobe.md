# modprobe

> Add or remove modules from the Linux kernel.

- Pretend to load a module into the kernel, but don't actually do it:

`sudo modprobe --dry-run {{module_name}}`

- Load a module into the kernel:

`sudo modprobe {{module_name}}`

- Remove a module from the kernel:

`sudo modprobe --remove {{module_name}}`

- Remove a module and those that depend on it from the kernel:

`sudo modprobe --remove-dependencies {{module_name}}`

- Show a kernel module's dependencies:

`sudo modprobe --show-depends {{module_name}}`
