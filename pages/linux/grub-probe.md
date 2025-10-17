# grub-probe

> Probe device information for a particular path or device.
> More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dprobe.html>.

- Get GRUB filesystem module for a path:

`sudo grub-probe {{[-t|--target]}} fs {{/boot/grub}}`

- Get the system device containing a path:

`sudo grub-probe {{[-t|--target]}} device {{/boot/grub}}`

- Get GRUB disk name for a system device:

`sudo grub-probe {{[-d|--device]}} {{[-t|--target]}} drive {{/dev/sdX}}`

- Get filesystem UUID:

`sudo grub-probe {{[-t|--target]}} fs_uuid {{/boot/grub}}`

- Get filesystem label:

`sudo grub-probe {{[-t|--target]}} fs_label {{/boot/grub}}`

- Get MBR partition type code(two hexadecimal digits):

`sudo grub-probe {{[-t|--target]}} msdos_parttype {{/dev/sdX}}`

- Probe using a custom device map:

`sudo grub-probe {{[-m|--device-map]}} {{path/to/custom_device.map}} {{[-t|--target]}} drive {{/boot/grub}}`
