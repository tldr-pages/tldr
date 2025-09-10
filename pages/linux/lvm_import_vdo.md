# lvm_import_vdo

> Import a VDO volume created by the VDO manager into an LVM-managed logical volume (irreversible).
> More information: <https://manned.org/lvm_import_vdo>.

- Import a VDO volume with automatic names for the VG/LV:

`lvm_import_vdo {{/dev/mapper/vdo_volume}}`

- Import and set the destination VG/LV name:

`lvm_import_vdo {{[-n|--name]}} {{vg_name/lv_name}} {{/dev/mapper/vdo_volume}}`

- Show what would be done without changing anything:

`lvm_import_vdo --dry-run {{/dev/mapper/vdo_volume}}`

- Convert in place without using a temporary snapshot (less safe):

`lvm_import_vdo --no-snapshot {{/dev/mapper/vdo_volume}}`

- Verbose output and automatically answer "yes" to prompts:

`lvm_import_vdo {{[-v|--verbose]}} {{[-y|--yes]}} {{/dev/mapper/vdo_volume}}`

- Use a VDO manager configuration file during import:

`lvm_import_vdo --vdo-config {{path/to/vdo.conf}} {{/dev/mapper/vdo_volume}}`
