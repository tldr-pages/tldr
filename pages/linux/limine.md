# limine

> An advanced, portable, multiprotocol bootloader.
> See also: `limine-enroll-config`, `limine-entry-tool`, `limine-snapper-sync`.
> More information: <https://codeberg.org/Limine/Limine>.

- Install Limine to an MBR-partitioned disk:

`limine bios-install {{/dev/sdX}}`

- Install Limine to a GPT-partitioned disk with a specific BIOS boot partition:

`limine bios-install {{/dev/sdX}} {{partition_number}}`

- Install Limine to a disk image file:

`limine bios-install {{path/to/image.iso}}`

- Install Limine for modern UEFI systems (requires the `limine-entry-tool` package):

`limine-install`

- Update boot entries after a kernel upgrade (requires the `limine-entry-tool` package):

`limine-update`

- Scan for other operating systems to add to the boot menu (requires the `limine-entry-tool` package):

`limine-scan`
