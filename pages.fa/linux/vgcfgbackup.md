# vgcfgbackup

> پشتیبان‌گیری از فرادادهٔ پیکربندی گروه حجم در فایل‌ها (نه داده‌های کاربر).
> اطلاعات بیشتر: <https://manned.org/vgcfgbackup>.

- پشتیبان‌گیری از فرادادهٔ همهٔ گروه‌های حجم (به‌طور پیش‌فرض در `/etc/lvm/backup/`):

`sudo vgcfgbackup`

- پشتیبان‌گیری از فرادادهٔ گروه حجم مشخص:

`sudo vgcfgbackup {{vg_name}}`

- نوشتن پشتیبان در فایل مشخص:

`sudo vgcfgbackup {{[-f|--file]}} {{path/to/backup}} {{vg_name}}`

- پشتیبان‌گیری از چند VG با الگوی نام فایل (`%s` به نام VG تبدیل می‌شود):

`sudo vgcfgbackup {{[-f|--file]}} {{/tmp/vg-backup-%s}} {{vg1 vg2 ...}}`

- افزایش جزئیات خروجی (برای جزئیات بیشتر `-v` را تکرار کنید):

`sudo vgcfgbackup {{[-v|--verbose]}} {{vg_name}}`
