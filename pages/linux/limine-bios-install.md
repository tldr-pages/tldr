# limine-bios-install

> Install the Limine bootloader on a disk for BIOS systems.
> This command writes the bootloader stages to a specified disk or image file.
> More information: <https://codeberg.org/Limine/Limine/src/branch/trunk/USAGE.md#biosmbr>.

- Install Limine to an MBR-partitioned disk:

`limine bios-install {{/dev/sdX}}`

- Install Limine to a GPT-partitioned disk with a specific BIOS boot partition:

`limine bios-install {{/dev/sdX}} {{partition_number}}`

- Install Limine to a disk image file:

`limine bios-install {{path/to/image.iso}}`
