# limine

> Limine Bootloader — modular BIOS/UEFI bootloader manager.
> Provides tools for installing, scanning, and managing Limine boot entries.
> More information: <https://limine-bootloader.org/docs/latest/>.

- Display help information:
`limine --help`

- Show the installed Limine version:
`limine --version`

- Install Limine to the default target (auto-detect disk or EFI partition):
`limine install`

- Install Limine to a specific disk device:
`limine install {{/dev/sdX}}`

- Install Limine into a specific EFI directory:
`limine install --efi-dir {{/boot/efi}}`

- Scan system for Limine-compatible boot entries:
`limine scan`

- Enroll a configuration file into the firmware (secure boot):
`limine enroll-config {{/boot/limine.conf}}`

- Reset Limine configuration enrollment:
`limine reset-enroll`

- Generate or update a Limine configuration template:
`limine config --generate`

- Update the Limine installation (refresh bootloader files):
`limine update`

- View or edit existing boot entries interactively:
`limine entry-tool --edit`

- Create a new Limine initramfs preset for mkinitcpio:
`limine mkinitcpio --preset {{preset_name}}`

- Display all Limine subcommands and their usage:
`limine help`
