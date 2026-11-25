# qm disk

> مدیریت تصاویر دیسک.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- افزودن `n` گیگابایت به دیسک مجازی:

`qm {{[di|disk]}} {{[resi|resize]}} {{100}} {{disk_name}} +{{n}}G`

- انتقال دیسک مجازی:

`qm {{[di|disk]}} {{[m|move]}} {{100}} {{scic0}} {{destination_storage_name}}`

- حذف نسخهٔ قبلی دیسک مجازی:

`qm {{[di|disk]}} {{[m|move]}} {{100}} {{scic0}} {{destination_storage_name}} --delete`

- وارد کردن تصویر دیسک VMDK، `.qcow2` یا خام با نام فضای ذخیره‌سازی مشخص:

`qm {{[di|disk]}} {{[i|import]}} {{100}} {{path/to/disk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`

- پویش مجدد همهٔ فضاهای ذخیره‌سازی و به‌روزرسانی اندازهٔ دیسک‌ها و تصاویر دیسک استفاده‌نشده:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- شبیه‌سازی پویش مجدد بدون نوشتن تغییرات در پیکربندی‌ها:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- تعیین ماشین مجازی با شناسهٔ آن:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`

- حذف دیسک:

`qm {{[di|disk]}} {{[u|unlink]}} {{100}} --idlist {{unused0,unused1,scsi1,...}}`
