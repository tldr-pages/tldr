# limine

> An advanced, portable, multiprotocol bootloader.
> Some tools such as `limine-bios-install`, `limine-install`, and `limine-update` have their own usage documentation.
> More information: <https://limine-bootloader.org/>.

- Install Limine on a disk for legacy BIOS systems:

`limine bios-install {{/dev/sdX}}`

- Install Limine for modern UEFI systems (requires the `limine-entry-tool` package):

`limine-install`

- Update boot entries after a kernel upgrade (requires the `limine-entry-tool` package):

`limine-update`

- Scan for other operating systems to add to the boot menu (requires the `limine-entry-tool` package):

`limine-scan`

- Synchronize Btrfs snapshots from Snapper to the boot menu (requires the `limine-snapper-sync` package):

`limine-snapper-sync`

- Enroll the configuration file's hash into the EFI binary for Secure Boot:

`limine-enroll-config {{path/to/BOOTX64.EFI}} {{blake2b_hash}}`
