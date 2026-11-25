# pkgctl repo

> مدیریت مخازن بسته‌بندی Git و پیکربندی آن‌ها برای Arch Linux.
> اطلاعات بیشتر: <https://manned.org/pkgctl-repo>.

- رونوشت‌گیری از مخزن بسته (نیازمند تنظیم کلید SSH در حساب GitLab مربوط به Arch Linux):

`pkgctl repo clone {{pkgname}}`

- رونوشت‌گیری از مخزن بسته از طریق HTTPS:

`pkgctl repo clone --protocol https {{pkgname}}`

- ایجاد مخزن بستهٔ جدید GitLab و رونوشت‌گیری پس از ایجاد (نیازمند احراز هویت معتبر API مربوط به GitLab):

`pkgctl repo create {{pkgbase}}`

- تغییر مخزن بسته به نسخهٔ مشخص:

`pkgctl repo switch {{version}} {{pkgbase}}`

- باز کردن وب‌سایت مخزن بسته:

`pkgctl repo web {{pkgbase}}`
