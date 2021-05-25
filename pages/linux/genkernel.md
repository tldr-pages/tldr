# genkernel

> Gentoo Linux utility to compile and install kernels.

- Automatically compile and install a generic kernel:

`sudo genkernel all`

- Build and install the bzImage|initramfs|kernel|ramdisk only:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- Apply changes to the kernel configuration before compiling and installing:

`sudo genkernel --menuconfig all`

- Generate a kernel with a custom name:

`sudo genkernel --kernname={{custom_name}} all`

- Use a kernel source outside of the default directory `/usr/src/linux`:

`sudo genkernel --kerneldir={{path/to/directory}} all`
