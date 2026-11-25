# vgchange

> تغییر ویژگی‌های گروه حجم مدیر حجم منطقی (LVM).
> همچنین : `lvm`.
> اطلاعات بیشتر: <https://manned.org/vgchange>.

- تغییر وضعیت فعال‌سازی حجم‌های منطقی در همهٔ گروه‌های حجم:

`sudo vgchange {{[-a|--activate]}} {{y|n}}`

- تغییر وضعیت فعال‌سازی حجم‌های منطقی در گروه حجم مشخص (با `vgscan` تعیین کنید):

`sudo vgchange {{[-a|--activate]}} {{y|n}} {{volume_group}}`
