# pvesm add

> افزودن فضاهای ذخیره‌سازی.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pvesm.1.html#cli_pvesm_add>.

- افزودن فضای ذخیره‌سازی دایرکتوری:

`pvesm {{[ad|add]}} dir {{storage_name}} --path {{path/to/directory}}`

- افزودن فضای ذخیره‌سازی LVM:

`pvesm {{[ad|add]}} lvm {{storage_name}} --vgname {{volume_group_name}}`

- افزودن فضای ذخیره‌سازی LVM-Thin:

`pvesm {{[ad|add]}} lvmthin {{storage_name}} --vgname {{volume_group_name}} --thinpool {{logical_volume_name}}`
