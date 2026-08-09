# akmods

> Automatic Kernel Module management system for Fedora/RHEL-based distributions.
> Rebuilds out-of-tree kernel modules (like NVIDIA drivers) dynamically when kernels update.
> More information: <https://manned.org/man/fedora-43/akmods>.

- Rebuild all missing or outdated kernel modules for the currently running kernel:

`sudo akmods`

- Forcefully rebuild all kernel modules regardless of current status:

`sudo akmods --rebuild --force`

- Rebuild modules specifically for a targeted kernel version:

`sudo akmods --kernel {{kernel_version}}`

- Display the current status and log details of the background akmods service:

`systemctl status akmods`
