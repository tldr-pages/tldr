# pvesh

> تعامل با API مربوط به Proxmox VE.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pvesh.1.html>.

- فهرست کردن گره‌های موجود:

`pvesh {{[g|get]}} /nodes`

- نمایش اطلاعات مفصل کانتینرها یا ماشین‌های مجازی:

`pvesh {{[g|get]}} /nodes/{{node_name}}/{{lxc|qemu}}`

- کشف مسیرهای API:

`pvesh {{[l|ls]}} {{/}}`

- نمایش دستورالعمل استفاده از مسیر API:

`pvesh {{[u|usage]}} {{/pools}}`

- افزودن استخر thin جدید به Proxmox:

`pvesh create /storage --storage {{storage_id}} --vgname {{volume_group}} --type lvmthin --thinpool {{thinpool_name}} --content {{content_type1,content_type2,...}}`
