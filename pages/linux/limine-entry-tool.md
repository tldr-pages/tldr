# limine-entry-tool

> A helper script to manage Limine bootloader entries on UEFI systems.
> More information: <https://gitlab.com/Zesko/limine-entry-tool>.

- Scan for other active UEFI boot entries and add them to the Limine menu:

`limine-entry-tool --scan`

- Add a new kernel boot entry with an initramfs and a kernel file:

`limine-entry-tool --add "{{kernel_name}}" "{{path/to/initramfs}}" "{{path/to/vmlinuz}}"`

- Add a new Unified Kernel Image (UKI) boot entry:

`limine-entry-tool --add-uki "{{kernel_name}}" "{{path/to/uki.efi}}"`

- Remove a kernel boot entry and its associated files from the ESP:

`limine-entry-tool --remove "{{kernel_name}}"`

- Remove an entire OS entry by its name or machine ID:

`limine-entry-tool --remove-os "{{OS_name|machine_id}}"`

- Add an EFI boot entry for an alternative bootloader (e.g., Windows):

`limine-entry-tool --add-efi "{{EFI_entry_name}}" "{{path/to/loader.efi}}"`
