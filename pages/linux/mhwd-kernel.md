# mhwd-kernel

> Manage and install Linux kernels in Manjaro.
> More information: <https://wiki.manjaro.org/index.php/Manjaro_Kernels>.

- List all available kernels:

`mhwd-kernel {{[-l|--list]}}`

- List all installed kernels:

`mhwd-kernel {{[-li|--listinstalled]}}`

- Install a kernel:

`sudo mhwd-kernel {{[-i|--install]}} {{kernel}}`

- Remove a kernel:

`sudo mhwd-kernel {{[-r|--remove]}} {{kernel}}`

- Install a kernel, replacing the currently running kernel:

`sudo mhwd-kernel {{[-i|--install]}} {{kernel}} rmc`
