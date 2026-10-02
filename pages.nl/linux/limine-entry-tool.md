# limine-entry-tool

> Een hulpscript om Limine-bootloader-items te beheren op UEFI-systemen.
> Meer informatie: <https://gitlab.com/Zesko/limine-entry-tool>.

- Scan naar andere actieve UEFI-boot-items en voeg ze toe aan het Limine-menu:

`limine-entry-tool --scan`

- Voeg een nieuw kernel-boot-item toe met een initramfs en een kernelbestand:

`limine-entry-tool --add "{{kernel_naam}}" "{{pad/naar/initramfs}}" "{{pad/naar/vmlinuz}}"`

- Voeg een nieuw Unified Kernel Image (UKI) boot-item toe:

`limine-entry-tool --add-uki "{{kernel_naam}}" "{{pad/naar/uki.efi}}"`

- Verwijder een kernel-boot-item en de bijbehorende bestanden van de ESP:

`limine-entry-tool --remove "{{kernel_naam}}"`

- Verwijder een volledig OS-item op basis van zijn naam of machine-ID:

`limine-entry-tool --remove-os "{{os_naam|machine_id}}"`

- Voeg een EFI-boot-item toe voor een alternatieve bootloader (bijv. Windows):

`limine-entry-tool --add-efi "{{efi_item_naam}}" "{{pad/naar/loader.efi}}"`
