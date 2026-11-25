# qm delsnapshot

> حذف snapshotهای ماشین مجازی.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_delsnapshot>.

- حذف snapshot:

`qm {{[del|delsnapshot]}} {{100}} {{snapshot_name}}`

- حذف snapshot از فایل پیکربندی (حتی اگر حذف snapshot دیسک شکست بخورد):

`qm {{[del|delsnapshot]}} {{100}} {{snapshot_name}} --force 1`
