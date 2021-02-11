# pacstrap

> Install packages using Pacman to the specified new root directory.
> More information: <https://man.archlinux.org/man/pacstrap.8>.

- Install the `base` package, Linux kernel and firmware for common hardware:

`pacstrap {{path/to/new/root}} {{base}} {{linux}} {{linux-firmware}}`

- Install the `base` package, Linux LTS kernel and `base-devel` build tools:

`pacstrap {{path/to/new/root}} {{base}} {{base-devel}} {{linux-lts}}`

- Install packages without copy the host's mirrorlist to the target:

`pacstrap -M {{path/to/new/root}} {{packages}}`

- Use an alternate configuration file for Pacman:

`pacstrap -C {{path/to/pacman.conf}} {{path/to/new/root}} {{packages}}`

- Install packages using the package cache on the host instead of on the target:

`pacstrap -c {{path/to/new/root}} {{packages}}`

- Install packages without copy the host's pacman keyring to the target:

`pacstrap -G {{path/to/new/root}} {{packages}}`

- Install packages in interactive mode (prompts for confirmation):

`pacstrap -i {{path/to/new/root}} {{packages}}`

- Install packages using package files:

`pacstrap -U {{path/to/new/root}} {{path/to/package1}} {{path/to/package2}}`
