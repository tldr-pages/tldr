# depmod

> Generate `modules.dep` and map files for Linux kernel modules.
> See also: `modprobe`.
> More information: <https://manned.org/depmod>.

- Generate dependency and map files for the current kernel:

`depmod`

- Generate dependency and map files in a specified directory:

`depmod {{[-o|--outdir]}} {{path/to/directory}}`

- Generate dependency and map files for a specific kernel version:

`depmod {{kernel_version}}`

- Examine a specific module instead of all modules:

`depmod {{kernel_version}} /{{path/to/module.ko}}`

- Use an alternative root filesystem directory:

`depmod {{[-b|--basedir]}} {{path/to/root_directory}}`

- Write dependency information to `stdout` instead of writing to files:

`depmod {{[-n|--dry-run]}}`
