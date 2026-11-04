# sbpctl

> Manage the systemd-boot-password boot manager, a systemd-boot fork with a password-protected editor.
> See also: `bootctl`.
> More information: <https://github.com/kitsunyan/systemd-boot-password#boot-manager-installing-and-configuration>.

- Install the boot manager into the EFI system partition:

`sudo sbpctl install /{{path/to/efi_system_partition}}`

- Install the boot manager only as the default EFI loader (`/EFI/BOOT/BOOT*.EFI`):

`sudo sbpctl install {{[-d|--default]}} /{{path/to/efi_system_partition}}`

- Install the boot manager with `/etc/sbp/loader.conf` included in the EFI binary:

`sudo sbpctl install {{[-i|--include]}} /{{path/to/efi_system_partition}}`

- Install the boot manager and sign it for Secure Boot with the keys in `/etc/sbp`:

`sudo sbpctl install {{[-s|--sign]}} /{{path/to/efi_system_partition}}`

- Generate a SHA-512 hash of a password for the `password` option in `loader.conf`:

`sbpctl generate`

- Create a standalone EFI application from a Linux EFI application and an initramfs:

`sudo sbpctl standalone {{[-i|--initrd]}} {{path/to/initramfs.img}} {{path/to/vmlinuz}} {{path/to/output.efi}}`
