# qm snapshot

> ایجاد snapshotهای ماشین مجازی.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_snapshot>.

- ایجاد snapshot از ماشین مجازی مشخص (نام باید با حرف آغاز شود):

`qm {{[sn|snapshot]}} {{100}} {{snapshot_name}}`

- ایجاد snapshot با توضیح مشخص:

`qm {{[sn|snapshot]}} {{100}} {{snapshot_name}} --description {{description}}`

- ایجاد snapshot شامل وضعیت ماشین مجازی در حال اجرا:

`qm {{[sn|snapshot]}} {{100}} {{snapshot_name}} --description {{description}} --vmstate 1`

- فهرست کردن snapshotهای ماشین مجازی:

`qm {{[lists|listsnapshot]}} {{100}}`

- بازگرداندن وضعیت ماشین مجازی مشخص به snapshot مشخص:

`qm {{[ro|rollback]}} {{100}} {{snapshot_name}}`
