# bootctl

> Control EFI firmware boot settings and manage boot loader.
> See also: `kernel-install`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/bootctl.html>.

- Show information about the system firmware and the bootloaders:

`bootctl`

- Show all available bootloader entries:

`bootctl list`

- Set a boot entry as the default to boot to:

`sudo bootctl set-default {{entry_id}}`

- Set a flag to boot into the system firmware on the next boot (similar to `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Specify the path to the EFI system partition (defaults to `/efi/`, `/boot/`, or `/boot/efi`):

`bootctl --esp-path /{{path/to/efi_system_partition}}/`

- Install `systemd-boot` into the EFI system partition:

`sudo bootctl install`

- Remove all installed versions of `systemd-boot` from the EFI system partition:

`sudo bootctl remove`
